# 云云科技顧問公司是一家幫忙企業客戶規劃實體主機轉成虛擬主機的諮詢服務公司,而使用雲端虛擬主機平台主要的好處,就是讓硬體資源可以集中共享,並透過平台有效率及彈性地分派硬體資源給實際需要的系統,不但可以因為減少主機的數量達到節能減碳,還可以為公司省下許多經費開銷。專案經理小楊,他的其中一項工作就是幫忙客戶整理各個系統運行實際需要的硬體資源,並依照系統執行的忙碌時段計算出實際需要的各項硬體資源總數,提供給企業客戶作為購置硬體之參考。
# 假定所有系統一旦開始執行後,就會固定以 D 天為一個週期重複執行(如下圖),且除了系統執行之忙碌時段外,其他都是閒置時間。當處於忙碌時段時,資源會被佔住,如果在相同時段有很多系統同時在忙碌時,就必須提供更多的硬體資源,才能確保這些系統能正常執行;反之,當系統閒置時,其所擁有的硬體資源會被雲端主機平台回收,並轉給其他需要硬體資源的系統。需要統計的硬體資源包含系統執行所需的核心(core)數、記憶體數(按每 GB 計)以及網路流量(按每 MB 計),而系統忙碌的時間皆以整點小時計,你的任務就是要幫小楊寫一個程式,能自動統計每個企業客戶在固定時間週期 D 內,任一時間下可能需要準備的各種硬體資源總數。

# Input
# 第一列有兩個整數 n 與 D,中間以一個空白區隔,分別代表此資料檔有 n 群的資料要分別統計,1 ≤ n ≤ 10,D 為一個定值,表其所有系統忙碌時間將以 D 天為一個週期循環。資料群由第二列開始,每群資料開頭的第一列是一個整數 s,代表該群資料需處理的筆數,隨後每一列代表一筆系統運行時的資源需求資料,皆包含六個整數(TdTs Th Rcore Rram Rbw),數字間以一個空白隔開,前三個整數為執行的時間,分別表示系統於第 Td 天的整點 Ts 時開始執行,並一共持續執行了 Th 小時(1 ≤ Td ≤ D,0 ≤ Ts≤ 23,Th ≥ 0),但不會持續超過一個週期的總時數;後三個整數分別代表執行時所需要硬體資源,包含核心數 Rcore,1 ≤ Rcore ≤ 10;記憶體數 Rram GB,1 ≤ Rram ≤ 20;以及網路頻寬 Rbw MB,0 ≤ Rbw ≤ 30;例如整數序列: 3 10 15 2 4 3,則代表此系統在第三天上午 10 時起,連續執行 15 小時,至第四天凌晨 1 時止皆為該系統的忙碌時間,執行時需要 2 個核心、4GB 的記憶體以及 3MB 的網路流量才能順利運行。每群資料的最後一列,以一個數字「0」,代表該群資料的結束。請注意,這些硬體資源需求資料並未事先排序。

# Output
# 每一列為統計每群資料會同時用到的最大資源數,應包含三個整數(每一個整數皆小於 30,000),分別代表同時間可能用到的最大核心數、最大記憶體數,以及最大網路頻寬數值。整數間以一個空白作為區隔。

# Sample Input #1
# 2 3
# 3
# 2 5 7 2 3 1
# 1 10 18 3 10 2
# 3 17 3 1 1 1
# 0
# 2
# 2 9 21 4 4 5
# 1 16 8 2 10 1
# 0

# Sample Output #1
# 3 10 2
# 4 10 5

# Sample Input #2
# 1 5
# 8
# 5 8 12 2 4 2
# 1 10 19 1 2 4
# 2 12 5 2 1 10
# 2 9 13 3 2 3
# 2 4 20 2 4 10
# 3 8 12 4 5 8
# 3 12 21 3 10 6
# 4 13 8 2 5 1
# 0

# Sample Output #2
# 7 15 23


def main():
    N, D = map(int, input().split())
    datasets = []

    for _ in range(N):
        dataset_length = int(input())
        dataset = []
        for _ in range(dataset_length):
            Td, Ts, Th, Rcore, Rram, Rbw = map(int, input().split())
            hour_start = (Td - 1) * 24 + Ts
            hour_end = hour_start + Th
            process_data = {
                "hour_start": hour_start,
                "hour_end": hour_end,
                "core_qty": Rcore,
                "ram_qty": Rram,
                "bandwidth_qty": Rbw,
            }
            dataset.append(process_data)
        input()  # Read the "0" at the end of each dataset
        datasets.append(dataset)

    res = []
    for dataset in datasets:
        processes_each_hour = [[] for _ in range(D * 24)]
        for process_id, data in enumerate(dataset):
            for i in range(data["hour_start"], data["hour_end"]):
                processes_each_hour[i % (D * 24)].append(process_id)

        max_core, max_ram, max_bandwidth = 0, 0, 0
        for processes in processes_each_hour:
            total_core, total_ram, total_bandwidth = 0, 0, 0
            for process_id in processes:
                data = dataset[process_id]
                total_core += data["core_qty"]
                total_ram += data["ram_qty"]
                total_bandwidth += data["bandwidth_qty"]
            max_core = max(max_core, total_core)
            max_ram = max(max_ram, total_ram)
            max_bandwidth = max(max_bandwidth, total_bandwidth)
        res.append([max_core, max_ram, max_bandwidth])

    # Output
    for r in res:
        print(" ".join(map(str, r)))


if __name__ == "__main__":
    main()
