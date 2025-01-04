import pandas as pd
from datetime import datetime

def load_files():
    ds = ".\\DS\\Monday-WorkingHours.pcap_ISCXml.csv" 
    df_mon_01 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Tuesday-WorkingHours.pcap_ISCX.csv" 
    df_mon_02= pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Wednesday-workingHours.pcap_ISCX_ml.csv" 
    df_mon_03 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv" 
    df_mon_04 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv" 
    df_mon_05 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Friday-WorkingHours-Morning.pcap_ISCX.csv" 
    df_mon_06 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv" 
    df_mon_07 = pd.read_csv(ds, encoding="utf-8")
    ds = ".\\DS\\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv" 
    df_mon_08 = pd.read_csv(ds, encoding="utf-8")

    
    df_mon_01= df_mon_01.reset_index(drop=True)
    df_mon_02= df_mon_02.reset_index(drop=True)
    df_mon_03= df_mon_03.reset_index(drop=True)
    df_mon_04= df_mon_04.reset_index(drop=True)
    df_mon_05= df_mon_05.reset_index(drop=True)
    df_mon_06= df_mon_06.reset_index(drop=True)
    df_mon_07= df_mon_07.reset_index(drop=True)
    df_mon_08= df_mon_08.reset_index(drop=True)
    

    dfs = [df_mon_01, df_mon_02, df_mon_03,df_mon_04,df_mon_05,df_mon_06,df_mon_07,df_mon_08]

    df_concat = pd.concat(dfs, ignore_index=True, axis=0)
    # Trimming the every column's name
    df_concat=df_concat.rename(str.strip, axis='columns')
    
    return df_concat

def generate_files(df_concat: pd.DataFrame ):
    path_root = ".\\DS\\out\\"
    df_concat.to_csv(path_root+"df_full.csv", index=False)
    print((path_root+"df_full.csv"))

    df_10p = df_concat.sample(frac=0.1)
    df_10p.to_csv(path_root+"df_10p.csv", index=False)
    print(path_root+"df_10p.csv")

    df_4_309p = df_concat.sample(frac=0.04309)
    df_4_309p.to_csv(path_root+"df_4_309p.csv", index=False)
    print(path_root+"df_4_309p.csv")

    df_20p = df_concat.sample(frac=0.2)
    df_20p.to_csv(path_root+"df_20p.csv", index=False)
    print(path_root+"df_20p.csv")

    df_33p = df_concat.sample(frac=0.33)
    df_33p.to_csv(path_root+"df_33p.csv", index=False)
    print(path_root+"df_33p.csv")

    df_10000 = df_concat.sample(n=10000)
    df_10000.to_csv(path_root+"df_10000.csv", index=False)
    print(path_root+"df_10000.csv")

    df_50000 = df_concat.sample(n=50000)
    df_50000.to_csv(path_root+"df_50000.csv", index=False)
    print(path_root+"df_50000.csv")
    
    df_100000 = df_concat.sample(n=100000)
    df_100000.to_csv(path_root+"df_100000.csv", index=False)
    print(path_root+"df_100000.csv")

    df_575000 = df_concat.sample(n=575000)
    df_575000.to_csv(path_root+"df_575000.csv", index=False)    
    print(path_root+"df_575000.csv")    



if __name__ == "__main__":
    init_time = datetime.now()
    print("start: ",init_time)
    df =load_files()
    generate_files (df)
    end_time = datetime.now()
    print("end: ", end_time)
    print("END")