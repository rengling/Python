if __name__ == "__main__":
    begin_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束页码:"))
    s_time = time.time()
    heima_forum(begin_page,end_page)
    e_time = time.time()
    print(f'总用时:{e_time-s_timme}秒')

    if __name__ == "__main__":
        s_time = time.time()
        heima =HeiMa()
        heima.run()
        e_time = time.time()
        print(f'总用时:{e_time - s_time}秒')