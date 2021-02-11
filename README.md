# Pdf-to-Image-converter
pdf를 image로 변환 후 저장합니다.  
사용 전 다음 절차를 거쳐주세요 !
```
pip install pdf2image
https://github.com/Belval/pdf2image
    => https://github.com/oschwartz10612/poppler-windows/releases/
    => Download Release-xx.xx.x.zip
use < poppler_path = r"C:\path\to\poppler-xx.xx.x\Library\bin" > as an argument in convert_from_path.
```

### 😎 python으로 처리하는게 덜 귀찮은 이유
pdf를 이미지로 변환하기 위해서는 보통 ...
1. pdf 변환 웹사이트를 켠다.
2. 파일을 업로드한다.
3. 변환된 zip파일을 다운로드 한다.
4. Downloads에 가서 압축 풀기를 누른다.
5. 압축을 풀고 싶은 폴더를 찾아서, 원하는 폴더 명으로 바꾸고 압축을 푼다.
6. 압축을 풀면 대부분 folder>folder>image들 형태다. 즉 폴더를 두번 타고 들어가야 한다.  
  폴더 안에서 다시 끌고 나와야함 ... 굉장히 귀찮음 .. 😑
7. 압축 파일을 지운다.  
  압축 푸는 것도 귀찮은데 지우기까지 해야한다. 🤬  
  
    
**하지만 간단히 코딩해서 돌리면 ~ 🥰**
* 폴더명, 이미지명을 내가 원하는 형태로 지정할 수 있고 (일일이 바꿀 필요 없이)
* 중첩 폴더가 생기거나 압축을 푸는 등의 귀찮음이 없음.
