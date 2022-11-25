loai_xe = int(input("Nhập loại xe:"))
so_km = float(input("Nhập số km: "))
time_cho = float(input("Cho biết thời gian chờ (số phút): "))
tien_cho = (time_cho-5)*800
if loai_xe == 4:
    if so_km <= 0.8:
        tien_cuoc = tien_cho + so_km*11000
    elif so_km <=20:
        tien_cuoc = (so_km-0.8)*12100 + 0.8*11000
    else:
        tien_cuoc = 0.8*11000 +(20-0.8)*121000 +(so_km-20)*10000
    print("Tiền cước = ", (tien_cuoc +tien_cho ))
if loai_xe == 7:
    if so_km <= 0.8:
        tien_cuoc = tien_cho + so_km*13000
    elif so_km <=30:
        tien_cuoc = (so_km-0.8)*14100 + 0.8*13000
    else:
        tien_cuoc = 0.8*13000 +(30-0.8)*141000 +(so_km-30)*12000
print("Tiền cước = ", (tien_cuoc +tien_cho ))

        
