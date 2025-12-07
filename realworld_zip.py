import os
import zipfile

# 여기만 너의 실제 루트 경로로 바꿔주면 됨
BASE_DIR = r"C:\Users\park9\OneDrive\문서\new_HAR\RealWorld2016"   # 예: "C:/Users/park9/realworld2016_dataset"
# Colab이면: BASE_DIR = "/content/drive/MyDrive/RealWorld/realworld2016_dataset"

# proband1 ~ proband9 만 대상으로 한다면:
proband_dirs = [f"proband{i}" for i in range(1, 16)]

for proband in proband_dirs:
    data_dir = os.path.join(BASE_DIR, proband, "data")
    if not os.path.isdir(data_dir):
        print(f"[경고] {data_dir} 가 존재하지 않아서 건너뜀")
        continue

    print(f"\n=== {proband} / data 폴더 처리 중 ===")
    for fname in os.listdir(data_dir):
        # acc_***_csv.zip, gyr_***_csv.zip 만 대상으로 하고 싶으면 아래 조건 사용
        if not (fname.endswith("_csv.zip") and (fname.startswith("acc_") or fname.startswith("gyr_"))):
            continue

        zip_path = os.path.join(data_dir, fname)
        extract_dir = os.path.join(data_dir, fname[:-4])  # ".zip" 제거한 폴더명

        # 이미 풀려 있으면 스킵 (여러 번 돌려도 안전하게)
        if os.path.exists(extract_dir):
            print(f"  [SKIP] {fname} -> 이미 {extract_dir} 존재")
            continue

        print(f"  [UNZIP] {fname} -> {extract_dir}")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(extract_dir)

print("\n모든 압축 해제 완료!")
