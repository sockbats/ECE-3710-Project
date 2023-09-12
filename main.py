# Data retrieved from https://world-weather.info/forecast/usa/provo/
import csv
import math
import random
import matplotlib.pyplot as plt


def main():
    temperatureData = {'2022-01-01': 19, '2022-01-02': 25, '2022-01-03': 32, '2022-01-04': 34,
                       '2022-01-05': 37, '2022-01-06': 43, '2022-01-07': 48, '2022-01-08': 36,
                       '2022-01-09': 34, '2022-01-10': 34, '2022-01-11': 34, '2022-01-12': 39,
                       '2022-01-13': 41, '2022-01-14': 34, '2022-01-15': 34, '2022-01-16': 36,
                       '2022-01-17': 34, '2022-01-18': 37, '2022-01-19': 34, '2022-01-20': 34,
                       '2022-01-21': 34, '2022-01-22': 34, '2022-01-23': 32, '2022-01-24': 36,
                       '2022-01-25': 34, '2022-01-26': 34, '2022-01-27': 34, '2022-01-28': 34,
                       '2022-01-29': 36, '2022-01-30': 37, '2022-01-31': 37, '2022-02-01': 30,
                       '2022-02-02': 27, '2022-02-03': 28, '2022-02-04': 30, '2022-02-05': 37,
                       '2022-02-06': 36, '2022-02-07': 41, '2022-02-08': 45, '2022-02-09': 43,
                       '2022-02-10': 45, '2022-02-11': 46, '2022-02-12': 46, '2022-02-13': 52,
                       '2022-02-14': 54, '2022-02-15': 45, '2022-02-16': 36, '2022-02-17': 39,
                       '2022-02-18': 43, '2022-02-19': 50, '2022-02-20': 52, '2022-02-21': 34,
                       '2022-02-22': 32, '2022-02-23': 23, '2022-02-24': 28, '2022-02-25': 27,
                       '2022-02-26': 28, '2022-02-27': 34, '2022-02-28': 41, '2022-03-01': 46,
                       '2022-03-02': 54, '2022-03-03': 57, '2022-03-04': 50, '2022-03-05': 41,
                       '2022-03-06': 34, '2022-03-07': 34, '2022-03-08': 36, '2022-03-09': 36,
                       '2022-03-10': 30, '2022-03-11': 36, '2022-03-12': 48, '2022-03-13': 30,
                       '2022-03-14': 41, '2022-03-15': 50, '2022-03-16': 46, '2022-03-17': 41,
                       '2022-03-18': 46, '2022-03-19': 52, '2022-03-20': 43, '2022-03-21': 36,
                       '2022-03-22': 43, '2022-03-23': 46, '2022-03-24': 54, '2022-03-25': 59,
                       '2022-03-26': 64, '2022-03-27': 68, '2022-03-28': 63, '2022-03-29': 52,
                       '2022-03-30': 55, '2022-03-31': 46}
    temperatures = []
    for key, value in temperatureData.items():
        temperatures.append(value)

    temperatures.sort()
    length = len(temperatures)

    # Mean
    mean = sum(temperatures) / length

    # Median
    if length // 2 % 1 != 0:
        median = temperatures[length // 2] + temperatures[(length // 2) + 1] / 2
    else:
        median = temperatures[length // 2]

    # Sample Variance
    sample_variance = 0
    for i in temperatures:
        sample_variance += (i - mean) ** 2
    sample_variance /= (length - 1)

    # Standard Deviation
    standard_deviation = math.sqrt(sample_variance)

    # Simple Random Sample
    random.seed(0)
    random_sample = sorted(random.sample(temperatures, 20))
    random_mean = sum(random_sample) / len(random_sample)
    random_length = len(random_sample)

    # SRS Sample Variance
    random_sample_variance = 0
    for i in random_sample:
        random_sample_variance += (i - random_mean) ** 2
    random_sample_variance /= (random_length - 1)

    # SRS Standard Deviation
    random_standard_deviation = math.sqrt(random_sample_variance)

    # Trimmed Means
    trimmed_data = temperatures[length // 20:-length // 20]
    trimmed_mean_5 = sum(trimmed_data) / len(trimmed_data)
    trimmed_data = temperatures[length // 10:-length // 10]
    trimmed_mean_10 = sum(trimmed_data) / len(trimmed_data)
    trimmed_data = temperatures[length // 5:-length // 5]
    trimmed_mean_20 = sum(trimmed_data) / len(trimmed_data)

    # Quartiles
    if length // 4 % 1 != 0:
        first_quartile = temperatures[length // 4] + temperatures[(length // 4) + 1] / 2
        third_quartile = temperatures[(length // 4) * 3] + temperatures[((length // 4) * 3) + 1] / 2
    else:
        first_quartile = temperatures[length // 4]
        third_quartile = temperatures[(length // 4) * 3]

    # Mode
    frequency = {}
    for item in temperatures:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1
    mode = max(frequency, key=frequency.get)

    # Final Output
    output = f"01. Mean: {mean:.3f}; Median: {median}\n" \
             f"02. Sample Variance: {sample_variance:.3f}; Standard Deviation: {standard_deviation:.3f}\n" \
             f"03. Simple Random Sample: {random_sample}\n   " \
             f"SRS Mean: {random_mean}; " \
             f"SRS Sample Variance: {random_sample_variance:.3f}; " \
             f"SRS Standard Deviation: {random_standard_deviation:.3f}\n" \
             f"04. This random sample does properly represent the entire data. The mean is very similar " \
             f"and the variance is much lower, meaning it more accurately represents the data.\n" \
             f"05. Trimmed Means:\n   " \
             f"5%: {trimmed_mean_5:.3f}\n   " \
             f"10%: {trimmed_mean_10:.3f}\n   " \
             f"20%: {trimmed_mean_20:.3f}\n" \
             f"06. First Quartile: {first_quartile}; Third Quartile: {third_quartile}\n" \
             f"07. Mode: {mode}; Median: {median}; See Dot Plot.png\n" \
             f"08. See Histogram.png\n" \
             f"09. There is an outlier of 68º, which occurred on March 27, 2022. See Box Plot.png\n" \
             f"10. Based on this data, the temperature during the first week of January " \
             f"would likely range between 30-50ºF, based on the mean of 40 and the standard deviation of 10"
    print(output)
    with open("Report.txt", "w") as f:
        f.write(output)
    dot_plot = {}
    x = []
    y = []
    for item in temperatures:
        if item not in dot_plot:
            dot_plot[item] = 1
            x.append(item)
            y.append(1)
        else:
            dot_plot[item] += 1
            x.append(item)
            y.append(dot_plot[item])
    plt.scatter(x, y)
    plt.title("Dot Plot of Temperatures in Provo (Jan-Mar 2022)")
    plt.xlabel("Temperature(°F)")
    plt.ylabel("Number of Occurences")
    plt.savefig("Dot Plot.png")
    plt.clf()
    plt.title("Histogram of Temperatures in Provo (Jan-Mar 2022)")
    plt.xlabel("Temperature(°F)")
    plt.ylabel("Number of Occurences")
    plt.hist(temperatures)
    plt.savefig("Histogram.png")
    plt.clf()
    plt.title("Box Plot of Temperatures in Provo (Jan-Mar 2022)")
    plt.xlabel("Temperature(°F)")
    plt.boxplot(temperatures, vert=False)
    plt.savefig("Box Plot.png")


if __name__ == '__main__':
    main()
