"""Teach-and-replay route recorder."""

from pybricks.parameters import Button, Color, Stop
from pybricks.tools import StopWatch, wait


STORAGE_OFFSET = 0
STORAGE_MAGIC = b"RTE1"
HEADER_SIZE = 6
SAMPLE_SIZE = 18
MAX_SAMPLES = 1000
SAMPLE_PERIOD_MS = 50


def pack_u16(value):
    value %= 65536
    return bytes((value % 256, value // 256))


def unpack_u16(data, offset):
    return data[offset] + data[offset + 1] * 256


def pack_s16(value):
    return pack_u16(value)


def unpack_s16(data, offset):
    value = unpack_u16(data, offset)
    return value - 65536 if value >= 32768 else value


def pack_s32(value):
    low = value % 65536
    high = (value // 65536) % 65536
    return bytes((low % 256, low // 256, high % 256, high // 256))


def unpack_s32(data, offset):
    low = unpack_u16(data, offset)
    high = unpack_u16(data, offset + 2)
    if high >= 32768:
        high -= 65536
    return high * 65536 + low


def pack_header(sample_count):
    return STORAGE_MAGIC + pack_u16(sample_count)


def unpack_header(header):
    if len(header) != HEADER_SIZE or header[:4] != STORAGE_MAGIC:
        return 0
    sample_count = unpack_u16(header, 4)
    return sample_count if sample_count <= MAX_SAMPLES else 0


def pack_sample(timestamp, left_angle, right_angle, left_speed, right_speed, heading):
    return (
        pack_u16(timestamp)
        + pack_s32(left_angle)
        + pack_s32(right_angle)
        + pack_s16(left_speed)
        + pack_s16(right_speed)
        + pack_s16(heading)
    )


def unpack_sample(sample):
    return (
        unpack_u16(sample, 0),
        unpack_s32(sample, 2),
        unpack_s32(sample, 6),
        unpack_s16(sample, 10),
        unpack_s16(sample, 12),
        unpack_s16(sample, 14),
    )


def storage_write(hub, offset, data):
    hub.system.storage(STORAGE_OFFSET + offset, write=data)


def storage_read(hub, offset, size):
    return hub.system.storage(STORAGE_OFFSET + offset, read=size)


def saved_sample_count(hub):
    """Return the number of saved samples, or zero if no route exists."""
    header = storage_read(hub, 0, HEADER_SIZE)
    if len(header) != HEADER_SIZE:
        return 0
    return unpack_header(header)


async def wait_for_record_or_replay(hub):
    """Wait for left to record or right to replay."""
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            while Button.LEFT in hub.buttons.pressed():
                await wait(20)
            return "record"
        if Button.RIGHT in pressed:
            while Button.RIGHT in hub.buttons.pressed():
                await wait(20)
            return "replay"
        await wait(50)


async def record_route(hub, left_motor, right_motor):
    """Record motor and gyro telemetry directly into persistent storage."""
    hub.light.on(Color.BLUE)
    hub.display.char("R")
    left_motor.stop(Stop.COAST)
    right_motor.stop(Stop.COAST)
    stopwatch = StopWatch()
    sample_count = 0
    storage_write(hub, 0, pack_header(0))

    while sample_count < MAX_SAMPLES:
        if Button.RIGHT in hub.buttons.pressed():
            break

        sample = pack_sample(
            stopwatch.time() % 65536,
            left_motor.angle(),
            right_motor.angle(),
            left_motor.speed(),
            right_motor.speed(),
            int(hub.imu.heading()),
        )
        storage_write(hub, HEADER_SIZE + sample_count * SAMPLE_SIZE, sample)
        sample_count += 1
        await wait(SAMPLE_PERIOD_MS)

    storage_write(hub, 0, pack_header(sample_count))
    hub.display.number(sample_count)
    await hub.speaker.beep(700, 150)
    print("Saved", sample_count, "route samples.")
    return sample_count


def read_sample(hub, sample_number):
    offset = HEADER_SIZE + sample_number * SAMPLE_SIZE
    return unpack_sample(storage_read(hub, offset, SAMPLE_SIZE))


async def replay_route(hub, robot, left_motor, right_motor):
    """Replay saved wheel encoder positions with recorded wheel speeds."""
    sample_count = saved_sample_count(hub)
    if sample_count < 2:
        hub.display.char("N")
        hub.light.on(Color.RED)
        print("No saved route. Press left to record one.")
        return

    hub.display.char("P")
    hub.light.on(Color.YELLOW)
    first_sample = read_sample(hub, 0)
    left_start = left_motor.angle()
    right_start = right_motor.angle()
    robot.stop()

    for sample_number in range(1, sample_count):
        sample = read_sample(hub, sample_number)
        left_target = left_start + sample[1] - first_sample[1]
        right_target = right_start + sample[2] - first_sample[2]
        left_speed = max(abs(sample[3]), 100)
        right_speed = max(abs(sample[4]), 100)

        await left_motor.run_target(left_speed, left_target, then=Stop.HOLD, wait=False)
        await right_motor.run_target(right_speed, right_target, then=Stop.HOLD, wait=False)
        while not left_motor.done() or not right_motor.done():
            await wait(10)

    robot.stop()
    print("Route replay completed.")


async def run2(hub, robot, left_motor, right_motor):
    """Record with left, then replay the saved route with right."""
    mode = await wait_for_record_or_replay(hub)
    if mode == "record":
        await hub.speaker.beep(700, 150)
        await record_route(hub, left_motor, right_motor)
    else:
        hub.display.char("P")
        hub.light.on(Color.YELLOW)
        await hub.speaker.beep(900, 150)
        await replay_route(hub, robot, left_motor, right_motor)