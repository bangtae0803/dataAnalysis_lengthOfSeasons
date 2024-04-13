{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Term Project 제안서"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# (1) 주제 선정 이유: <br>\n",
    "  우리나라의 특징에 대해 생각해보면 ‘사계절이 뚜렷하다’를 꼽을 수 있습니다. <br>\n",
    " 그러나 언젠가부터 봄가을이 거의 없어졌다시피 짧아지고, 여름과 겨울이 길어진 것과 같이 느껴집니다. <br>\n",
    " 이렇게 느껴지는 것이 과연 단순히 느낌인지, 실제로 계절의 길이가 변화하고 있는 것인지를 <br>통계를 기반으로 사실 확인을 해보기 위해 이를 Python 언어를 통해 획득하고 분석하는 작업을 이번 Term project의 주제로 선정하였습니다.\n",
    "# (2) 가설 정의: <br>\n",
    " ‘과거에 비해 현재 봄가을의 길이가 짧아졌고, 여름과 겨울의 길이가 길어졌다.’라는 명제를 이번 Term 프로젝트를 통해 증명하고자 합니다.\n",
    "# (3) 인터넷을 통한 데이터 획득: <br>\n",
    " 기상청 기상자료개방포털에서는 CSV 파일과 엑셀 파일을 통해 기온분석 통계의 데이터를 제공합니다. <br>\n",
    "이 데이터들을 파이썬에서 가공할 수 있도록 panda라는 모듈을 이용해 불러올 계획입니다.\n",
    "# (4) 분석을 위한 데이터의 가공: <br>\n",
    " 기상청에서 발간한 <기후변화감시 용어 해설집>에 따르면, <br>\n",
    "봄의 시작일은 ‘일평균 기온이 5도 이상으로 올라간 후 다시 떨어지지 않은 첫날부터’ <br>\n",
    "여름의 시작일은 ‘일평균 기온이 20도 이상으로 올라간 후 다시 떨어지지 않은 첫날부터’, <br>\n",
    "가을의 시작일은 ‘일평균 기온이 20도 미만으로 떨어진 후 다시 올라가지 않은 첫날부터’ <br>\n",
    "그리고 겨울의 시작일은 ‘일평균 기온이 5도 미만으로 떨어진 후 다시 올라가지 않은 첫날부터’로 정의 합니다.<br>\n",
    "또한 기온임계치를 이용해 계절일수를 발표하는데, 계절길이의 변화는 일평균기온을 9일 이동평균한 자료를 사용합니다.<br><br>\n",
    "따라서 기온이 떨어지지 않는 기간을 9일을 기준으로 하여 각 계절의 시작일로 정의하고 <br>panda를 통해 불러온 기온 분석 통계의 데이터들을 분석하여 연도별 각 계절들의 시작일을 구하고, <br>\n",
    "각 계절의 시작일에서 다음 계절의 시작일까지의 차를 계산하면 연도별 각 계절의 일 수를 구할 수 있습니다. <br>\n",
    "또한 위의 과정을 통해 구한 과거와 현재의 연도별 각 계절의 일 수 변화 경향을 한 눈에 파악할 수 있도록 Matplotlib을 이용해 그래프로 만들어 시각화 할 계획입니다.<br><br>\n",
    "\n",
    " 우선 csv 파일을 read 한 뒤 '날짜'와 '평균 기온'의 데이터들만 추출하여 이를 각각 리스트로 만든 뒤 <br>\n",
    "\n",
    " def spring(): #봄 시작 지점 탐색 함수 <br>\n",
    "    global i    <br>\n",
    "    \n",
    "    while(i<=len(date_list)-9) : \n",
    "        if float(avg_list[i])>=5.0\\\n",
    "           and float(avg_list[i+1])>=5.0\\\n",
    "                    and float(avg_list[i+2])>=5.0\\\n",
    "                        and float(avg_list[i+3])>=5.0\\\n",
    "                            and float(avg_list[i+4])>=5.0\\\n",
    "                                and float(avg_list[i+5])>=5.0\\\n",
    "                                    and float(avg_list[i+6])>=5.0\\\n",
    "                                        and float(avg_list[i+7])>=5.0\\\n",
    "                                            and float(avg_list[i+8])>=5.0 :\n",
    "                                            point.append(i)\n",
    "                                            i+=1\n",
    "                                            return i\n",
    "                                            break\n",
    "                   \n",
    "        else: i+=1\n",
    "\n",
    "이를 위와 같이 while과 for 반복문, if 조건문을 이용해 각 계절의 시작 지점들의 인덱스 구하고 <br>\n",
    "이를 모두 point 리스트안에 추가하였습니다.<br>\n",
    "그 이후 point[l+1]-point[l]과 같이 차이를 구하는 형태로 20년 동안의 각 계절들의 길이를 구하였습니다. <br>\n",
    "\n",
    "\n",
    "# (5) 분석 결과 도출: <br>\n",
    "우선 각 계절들의 길이를 구한 결과<br>\n",
    "봄 길이(일): [99, 76, 70, 77, 60, 88, 93, 76, 65, 72, 54, 61, 63, 74, 73, 78, 76, 105, 78, 93]<br>\n",
    "여름 길이(일): [120, 126, 135, 113, 134, 120, 119, 111, 112, 110, 123, 133, 135, 125, 132, 136, 127, 116, 118, 127]<br>\n",
    "가을 길이(일): [45, 68, 70, 61, 64, 54, 73, 72, 75, 67, 62, 58, 63, 76, 61, 35, 66, 53, 59, 73]<br>\n",
    "겨울 길이(일): [118, 105, 96, 119, 89, 99, 101, 106, 114, 122, 122, 97, 113, 82, 95, 116, 83, 111, 97]<br>\n",
    "\n",
    "위와 같은 데이터를 얻을 수 있었습니다.<br><br>\n",
    "그러나 이를 그래프로 나타내어 관찰해보니 이는 증명 하고싶은 가설인<br> ‘과거에 비해 현재 봄가을의 길이가 짧아졌고, 여름과 겨울의 길이가 길어졌다.’ 라는 명제를 증명할 수 있을만큼의 <br>경향성이나 추세를 보이지 않았으며, 변화 또한 상당히 큰 폭으로 나타났습니다.<br>\n",
    "따라서 ‘과거에 비해 현재 봄가을의 길이가 짧아졌고, 여름과 겨울의 길이가 길어졌다.’라는 명제가 사실이 아닌 <br>\n",
    "'평균 기온의 상승'과 같은 또 다른 이유에 의해 생겨난 잘못된 편견인지를 확인해보기 위해 20년 동안의 각 계절의 평균 기온을 분석해보았습니다<br><br>\n",
    "그 결과 <br>\n",
    "봄 평균 기온(˚C): [12.61, 13.59, 14.25, 15.6, 14.74, 13.83, 14.22, 16.33, 13.2, 14.89, 16.3, 13.94, 13.9, 15.84, 14.77, 14.1, 13.55, 13.49, 13.94, 14.02]    \n",
    "여름 평균 기온(˚C): [23.41, 22.7, 23.41, 23.98, 23.07, 23.84, 23.73, 23.87, 25.06, 24.04, 24.52, 24.48, 23.95, 24.22, 24.96, 24.2, 25.21, 24.8, 24.17, 24.75]<br>\n",
    "가을 평균 기온(˚C): [11.26, 11.48, 9.69, 11.43, 9.78, 10.18, 9.36, 10.05, 10.96, 12.38, 11.13, 8.78, 12.57, 8.74, 10.12, 12.9, 10.42, 11.95, 12.2, 8.2]     <br> \n",
    "겨울  평균 기온(˚C): [1.07, 0.88, -0.98, 0.18, 2.04, -0.08, 1.66, -0.6, -1.4, -0.11, -0.93, 0.41, 0.26, -0.55, -0.2, -1.35, -0.85, 2.36, 0.07]<br>\n",
    "라는 데이터를 얻었습니다. \n",
    "<br>이를 그래프로 나타내어 관찰해보니 봄, 가을, 겨울은 특별한 경향성이나 추세 없이 진동하는\n",
    "형태를 띄었고, <br>\n",
    "여름만 유일하게 진동하면서 우상향하는 그래프를 나타냈습니다.\n",
    "\n",
    "# (6) 결론: <br>\n",
    "본 프로젝트를 통해 증명하고자 한 가설은 ‘과거에 비해 현재 봄가을의 길이가 짧아졌고, 여름과 겨울의 길이가 길어졌다.’였습니다. <br>\n",
    "그러나 각 계절들의 길이를 분석한 결과 증가 또는 감소의 추세나 경향성 없이 진동하는 형태를 나타내었고 <br>\n",
    "각 계절들의 평균 기온 또한 여름의 그래프의 경우 진동하면서 우상향하였지만 다른 계절들의 경우 그렇지 않았고 특별한 경향성이나 추세 또한 보이지 않았습니다. <br>\n",
    "따라서 '계절의 길이가 변했다'를 '평균 기온의 상승'과 같은 또 다른 이유 때문에 생겨난 착각이라고 결론을 내리기에도 비약이 있다고 생각합니다. <br>\n",
    "따라서 이번 데이터 분석을 통해서 제 명제를 증명하고 확인하는 것에 실패하였습니다.<br><br>\n",
    "제 명제를 증명하고 확인하는 것에 실패한 이유를 생각해본 결과 그 이유는 크게 두 가지라고 생각합니다.<br>\n",
    "우선, '분석한 데이터의 수와 기간이 충분하지 않았다'입니다. <br>\n",
    "제가 이 가설을 증명하고 싶었던 이유는 제 체감상 2000년대에 비해 현재 활동하기 적합한 날씨의 계절인 봄가을이 짧아지고 몹시 더운 여름이나 몹시 추운 겨울이 늘었다고 생각했기 때문입니다.<br>\n",
    "따라서 저는 제가 경험적으로 느낀 가설을 증명하기 위해 2002년부터 2021년까지 총 20년의 데이터를 분석하였습니다.<br>\n",
    "그러나 분석 결과를 보니 최근 20년만의 데이터를 가지고는 계절의 변화를 관찰하기에 충분하지 않았던 것 같습니다.<br>\n",
    "실제로는 '지난 30년, 한국의 여름은 20일 길어지고 겨울은 22일 짧아졌다.'라는 기상청의 분석 결과가 있습니다.<br>\n",
    "그러나 이는 과거 약 30년(1912년부터 1940년)의 평균과 최근 30년(1991년부터 2020년)의 평균을 비교한 결과로,<br>\n",
    "계절의 길이 변화를 관찰하는 데에는 이 정도의 데이터의 수와 관찰 기간이 필요하다고 느꼈습니다.<br><br>\n",
    "두 번째로, 본 가설을 증명하는 데 사용한 '각 계절의 시작일 기준'이 적합하지 않았다고 생각합니다.<br>\n",
    "그 이유는 매년 각 계절들의 시작일, 길이, 평균 기온 등의 변화가 큰 폭으로 나타났기 때문입니다.<br>\n",
    "본 프로젝트를 통해 얻은 데이터를 그래프로 나타낸 것을 보면, 대부분의 그래프에서 특별한 경향성이나 추세가 없이 큰 폭으로 진동하는 것을 알 수 있습니다. <br>\n",
    "실제로, 본 데이터 분석에 사용한 '각 계절의 시작일 기준'을 통해 계산한 2011년과 2015년 겨울의 길이 차이는 약 40일입니다. <br>\n",
    "그러나 각 계절들의 시작일, 길이, 평균 기온 등이 매년 이렇게까지 큰 폭으로 차이가 난다는 것은 '각 계절의 시작일 기준'에 문제가 있다고 생각합니다.\n",
    "\n",
    "비록 본 프로젝트를 통해 제 명제를 증명하고 확인을 하지는 못 했지만 데이터 분석에 있어 충분한 양의 데이터가 얼마나 중요한 것인지, <br>\n",
    "그리고 많은 양의 데이터를 분석하는만큼 작은 조건 하나하나가 결과에 큰 차이를 만든다는 것,<br>\n",
    "마지막으로 인터넷 상에서 api, csv 등의 형태로 다양한 데이터들이 제공되므로 <br>\n",
    "저와 같은 일반인들도 이를 이용해 유의미한 분석을 해낼 수 있다는 것을 깨닫게 되었습니다.\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# (7) 참고 문헌\n",
    "- 민형기, 『파이썬으로 데이터 주무르기』, 비제이퍼블릭, 2017.<br>\n",
    "- 기상청 기후변화감시과, 『기후변화감시 용어 해설집』, 2020, p.75<br>\n",
    "- 구민주, 2021.05.08, [데이터 뉴스] 365일 중 118일이 여름…뜨거워진 한반도. 시사저널<br>\n",
    "http://www.sisajournal.com/news/articleView.html?idxno=216474<br>\n",
    "# (8) 별첨: (3)의 획득한 데이터 원본<br>\n",
    "- Weather_Data.csv(기상청 기상자료개방포털에서 제공하는 CSV 파일)<br>\n",
    "\n",
    "# (9) 별첨: (4)의 가공된 데이터 원본<br>\n",
    "- length_data.csv (20년간의 각 계절들의 길이 데이터)\n",
    "- avg_data.csv (20년간의 각 계절들의 평균 기온 데이터)\n",
    "\n",
    "# (10) 별첨: (3)을 (4)로 변환하는 등의 작업을 위하여 본인이 직접 개발한 Python 소스코드 원본 <br>\n",
    "\n",
    "- 2022103400_Term_Project.py\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
