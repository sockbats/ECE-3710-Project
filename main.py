# Data retrieved from https://world-weather.info/forecast/usa/provo/
# and placed into "Provo Weather Data.csv"
import csv
import math
import random
import matplotlib.pyplot as plt


def main():
    temperatures = []
    with open("Provo Weather Data.csv", "r") as csvFile:
        f = csv.reader(csvFile)
        next(f)
        for row in f:
            temperatures.append(int(row[1]))

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

    # Discuss answers???

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

    # Final Output
    output = f"1. Mean: {mean:.3f}; Median: {median}\n" \
             f"2. Sample Variance: {sample_variance:.3f}; Standard Deviation: {standard_deviation:.3f}\n" \
             f"3. Simple Random Sample: {random_sample}\n   " \
             f"SRS Sample Variance: {random_sample_variance:.3f}; " \
             f"SRS Standard Deviation: {random_standard_deviation:.3f}\n" \
             f"4. \n" \
             f"5. Trimmed Means:\n   " \
             f"5%: {trimmed_mean_5:.3f}\n   " \
             f"10%: {trimmed_mean_10:.3f}\n   " \
             f"20%: {trimmed_mean_20:.3f}\n" \
             f"6. First Quartile: {first_quartile}; Third Quartile: {third_quartile}"
    print(output)
    plt.hist(temperatures)
    plt.show()
    plt.boxplot(temperatures)
    plt.show()


if __name__ == '__main__':
    main()
