""" opencv �������� """
# 1. ��������
## win10 + python3.5/3.6 + opencv3.3/���߸��� + pycharm2017
## pip install opencv-python
## pip install openc-contrib_python
## pip install pytesseract

# 2. �γ�������Ŀ��
## opencv ͼ���дģ��
## opencv ͼ����ģ��
## opencv ���ֱ�̼���
## ���ð���
## Tesseract-OCR + opencv
## �����Ŀ��ʵ������


import cv2 as cv


src = cv.imread("CrystalLiu1.jpg")  # ����ͼƬ�Ž�src��

# ��������, ���ڿ��Ե�����С�� ���Ǳ�ǩ�ĳ�cv2.WINDOW_NORMAL��Ҳ�ɵ������ڴ�С��
# ��ͼ��ά��̫�� ����Ҫ��ӹ켣��ʱ���������ڴ�С���������
cv.namedWindow("Crystal Liu")

cv.imshow("Crystal Liu", src)  # ��srcͼƬ����ô����Ĵ�����
cv.waitKey(1000) # ���м��������1000ms���Զ�������������0��ʾֻ�ü������������
cv.destroyAllWindows()  # �ر����д���

# cv2.waitKey() ��һ�����̰󶨺�������Ҫָ����������ʱ��߶��Ǻ� �뼶��
# �����ȴ��ض��ļ����룬���Ƿ��м������롣
# �ض��ļ�����֮�ڣ���� �������������������᷵�ذ����� ASCII ��ֵ�����򽫻�������С�
# ���û �м������룬����ֵΪ -1���������������������Ĳ���Ϊ 0�������������� �ڵĵȴ��������롣
# ��Ҳ���Ա���������ض����Ƿ񱻰��£�

# cv2.destroyAllWindows() ��������ɾ���κ����ǽ����Ĵ��ڡ�
# ��� ����ɾ���ض��Ĵ��ڿ���ʹ�� cv2.destroyWindow()������������������ɾ ���Ĵ�������
