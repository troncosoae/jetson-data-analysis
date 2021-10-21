from data_works.general import get_df_from_file


if __name__ == '__main__':
    print('running')

    df1 = get_df_from_file('performance_data/benchmark_torch/torch/torch/cpu_-15_large_v1/batch_exec_times.csv')
    print(df1)
