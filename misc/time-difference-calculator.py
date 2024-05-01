# Time Difference Calculator

# 輸入兩個時間，格式為 HH:MM:SS，其中 HH 代表小時，範圍為 00 到 23；MM 代表分，範圍為 00 到 59；SS 代表秒，範圍為 00 到 59。請以相同格式輸出時間 1 到時間 2 的時間差。

# Sample Input #1
# 11:13:20
# 21:10:31
# Sample Output #1
# 09:57:11

# Sample Input #2
# 02:13:18
# 01:20:32
# Sample Output #2
# 23:07:14


def time_to_sec(t: str) -> int:
    times_str = t.split(":")
    times = list(map(int, times_str))
    return times[0] * 3600 + times[1] * 60 + times[2]


def sec_to_time(s: int) -> str:
    if s < 0:
        s += 24 * 3600  # Move time difference to the next day

    h = s // 3600
    s -= h * 3600
    m = s // 60
    s -= m * 60
    return f"{h:02}:{m:02}:{s:02}"


def calc_time_diff(t1: str, t2: str) -> str:
    t1_in_sec = time_to_sec(t1)
    t2_in_sec = time_to_sec(t2)
    diff_in_sec = t2_in_sec - t1_in_sec
    return sec_to_time(diff_in_sec)


def time_diff_calculator():
    print("### Time Difference Calculator ###")
    print("Please input two times with the format HH:MM:SS")
    t1 = input("Time 1: ")
    t2 = input("Time 2: ")
    time_diff = calc_time_diff(t1, t2)
    print(time_diff)


time_diff_calculator()
