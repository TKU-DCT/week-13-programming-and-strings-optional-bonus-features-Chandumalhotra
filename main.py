# main.py

# 1) Example CPU readings (you can change these numbers if you want)
cpu_readings = [45, 82, 77, 91, 88, 95]


# 2) Count how many times CPU usage exceeds a threshold (e.g. 80%)
def count_over_threshold(readings, threshold):
    count = 0
    for value in readings:
        if value > threshold:   # condition
            count += 1          # loop + condition
    return count


# 3) Generate a text-based system summary (string formatting)
def make_summary(readings):
    if len(readings) == 0:
        return "No CPU data.\n"

    # calculate average manually (using a loop)
    total = 0
    for value in readings:
        total += value
    avg = total / len(readings)

    max_cpu = max(readings)
    min_cpu = min(readings)

    over_80 = count_over_threshold(readings, 80)
    over_90 = count_over_threshold(readings, 90)

    # build a multi-line string
    summary = ""
    summary += "CPU SUMMARY\n"
    summary += "-----------\n"
    summary += f"All readings      : {readings}\n"
    summary += f"Total samples     : {len(readings)}\n"
    summary += f"Average CPU       : {avg:.2f}%\n"
    summary += f"Maximum CPU       : {max_cpu}%\n"
    summary += f"Minimum CPU       : {min_cpu}%\n"
    summary += f"Times CPU > 80%   : {over_80}\n"
    summary += f"Times CPU > 90%   : {over_90}\n"
    return summary


# 4) Simulate email alerts when CPU > 90%
def simulate_email_alerts(readings):
    print("\nEMAIL ALERTS")
    print("------------")

    any_alerts = False
    for value in readings:
        if value > 90:
            any_alerts = True
            # very simple "fake email" text
            print(f"[EMAIL] To: admin@example.com")
            print(f"Subject: HIGH CPU ALERT - {value}%")
            print(f"Body   : CPU is {value}% which is above 90%\n")

    if not any_alerts:
        print("No CPU > 90%, no alerts.\n")


# 5) Save summary to a text file
def save_summary_to_file(summary_text):
    filename = "system_summary.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary_text)
    print(f"Summary saved to {filename}")


# 6) main function
def main():
    summary = make_summary(cpu_readings)

    # print summary (for screenshot)
    print(summary)

    # simulate email alerts
    simulate_email_alerts(cpu_readings)

    # save summary to file
    save_summary_to_file(summary)


if __name__ == "__main__":
    main()
