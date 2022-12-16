# :grin: HAPPY Entertainment Dataset :grin:
네이버 부스트캠프 NLP 6조 HAPPY팀이 제작한 국내 예능 domain-specific dataset입니다.  
이 데이터셋은 Relation Extraction Task를 위해 제작되었으며 [한국어 위키백과](https://ko.wikipedia.org/wiki/)를 크롤링했습니다.


> :heavy_exclamation_mark: **DISCLAIMER :heavy_exclamation_mark: 
> 본 Dataset은 혐오 및 차별적 표현을 포함하고 있을 수 있습니다. 열람에 주의하세요**  

### Dataset Size
```full dataset``` : 1663  
```train dataset``` : 1332  
```valid dataset``` : 167  
```test dataset```: 168  


## :closed_book: Dataset Description
### Label Distribution
![label distribution](https://user-images.githubusercontent.com/112468961/208037405-f3998b65-8bd1-4f19-b868-7eeab0cc494f.png)


### Length Distribution
![sentlen distribution](https://user-images.githubusercontent.com/112468961/208037423-bc661d07-c84e-475b-84bf-131791d7fb70.png)

## :blue_book: Relation Map & Guideline & Example Sentences
**Guideline:**
[6조(HAPPY)-예능 가이드라인.pdf](https://github.com/boostcampaitech4lv23nlp1/level2_dataannotation_nlp-level2-nlp-06/files/10243267/6.HAPPY.-.pdf)

**Relation map:**
|class_name(ko)|class_name(eng)|direction(sub, obj)|description|
|--|--|--|--|
|관계_없음|no_relation|(*,*)|관계를 유추할 수 없거나 정의된 relation 으로 분류할 수 없음|
|단체:별칭|org:alternate_name|(ORG,ORG)|object는 subject의 별칭|
|단체:소속인|org:employee|(ORG,PER)|object는 subject에 종사하는 사람|
|단체:프로그램|org:program|(ORG,PRO)|object는 subject의 프로그램|
|인물:별칭|per:alternate_name|(PER:PER/POH)|object는 subject의 별칭|
|인물:동료|per:colleagues|(PER:PER)|object는 subject와 문장 내 공통 소속 명시되어 있는 사람|
|인물:사건|per:event|(PER:POH)|object는 subject가 연루된 사건|
|인물:소속단체|per:member_of|(PER:ORG)|object는 subject가 속했던/속한 단체|
|인물:참여프로그램|per:participate_in|(PER:PRO)|object는 subject가 참여할/참여하는/참여했던 프로그램|
|인물:직업/직함|per:title|(PER:POH)|object는 subject의 과거/현재 직업/직함|
|프로:방송시간|pro:air_time|(PRO:DAT)|object는 subject의 방송 시작, 종료, 지속시간|
|프로:종영일|pro:end_at|(PRO:DAT)|object는 subject의 종영일|
|프로:방영시작일|pro:start_at|(PRO:DAT)|object는 subject의 방영시작일|
|프로:하위_프로|pro:subprogram|(PRO:PRO/POH)|object는 subject내 코너/에피소드/시즌|

**Example Sentences**

```org:alternate_name```:이후 국내 최초의 민간 방송인 CBS기독교방송, 1954년 12월 15일에 개국하였고, 부산에서 최초의 상업 방송인 문화방송(MBC)이 1961년 12월에 개국하였다.<br>  
```org:employee```:유재석은 심형래와는 영화 촬영을 통해 같이 인연을 맺어온 사이이며 KBS 공채 7기 개그맨으로서 KBS 공채 개그맨 중 꽃이라 불리는 7기 멤버들과도 깊은 친분을 유지하고 있다.<br>  
```org:program```:《세계테마기행》은 대한민국의 EBS 1TV에서 매주 월요일부터 금요일까지 저녁 8시 40분에 방송 중인 여행 전문 교양 프로그램이다.<br>  
```per:alternate_name```:이 시기에 무한도전에 특별히 출연했던 게스트들로는 배우 차승원, 세계 테니스의 요정 마리아 샤라포바 등이 있다. 1기의 마지막 편에서는 '놀이기구에서 립스틱 바르기'가 도전 과제였으며, 게스트로 그룹 슈가가 출연하였다.<br>  
```per:colleagues```:5회 자유여행은 명품 조연 특집으로 강호동과 성동일이 대장을 맡았다.<br>  
```per:event```:이는 결국 프라이머리의 표절 의혹으로 이어졌고, 카로 에메랄드 측에서도 "표절이 맞다."라고 입장을 표하였다.<br>  
```per:member_of```:그 이후 컨츄리 꼬꼬는 대박이 났으며 신정환과 탁재훈이 엄청나게 유명세를 탔는데 탁재훈은 이 유명세를 이용해서 영화 배우로 데뷔하고 김수미와 같이 여러 영화를 촬영했다.<br>  
```per:participate_in```:탁재훈은 그 탓에 생계에 곤란을 겪었으며 생계 때문에 경찰청 사람들에서 단역으로 출연하여 범죄자(도둑) 역할을 했다.<br>  
```per:title```:유재석(劉在錫, Yu Jae-Seok, 1972년 8월 14일 ~ )은 대한민국의 방송인, MC, 희극 배우이다.<br>  
```pro:air_time```:《TV 동물농장》은 매주 일요일 오전 9시 30분에 방송되는 동물 전문 교양 프로그램이다.<br>  
```pro:end_at```:무한도전은 2005년 4월 23일부터 2018년 3월 31일까지 MBC TV에서 방영되었던 텔레비전 프로그램이다.<br>  
```pro:start_at```:《개그콘서트》는 1999년 9월 4일부터 2020년 6월 26일까지 방송되었던 코미디 프로그램이다.<br>  
```pro:subprogram```:바스켓을 타고 올라가는 것에 대해 두려워하는 부분이 같은 방송사 프로그램 일요일 일요일 밤에의 코너인 '불가능은 없다'와 흡사하다는 내용이었다.<br><br>  



### Train Scores
|Pretrained Model|Micro F1|Auprc|Accuracy|
|--|--|--|--|
|klue/bert-base|87.649|90.582|0.8468|
|klue/roberta-small|81.633|81.783|0.8138|
|klue/roberta-base|83.333|90.080|0.8288|
|klue/roberta-large|88.095|88.708|0.8559|
|monologg/koelectra-small-v3-discriminator|40.976|36.338|0.5045|
|monologg/koelectra-base-v3-discriminator|69.959|69.417|0.7087|
|jinmang2/kpfbert|85.600|84.315|0.8468|


## :man: Participants
PM : [류재환](https://github.com/risolate)

[김준휘](https://github.com/intrandom5),
[박수현](https://github.com/HitHereX),
[박승현](https://github.com/koohack),
[설유민](https://github.com/ymnseol)

## 📗 Wrap-up Report
[NLP_6조_데이터_제작_랩업_리포트.pdf](https://github.com/boostcampaitech4lv23nlp1/level2_dataannotation_nlp-level2-nlp-06/files/10243298/NLP_6._._._._.pdf)

 ## :bookmark_tabs: License
원문 출처 : https://ko.wikipedia.org/wiki/

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/CC_BY-SA_icon.svg/2560px-CC_BY-SA_icon.svg.png" width ='200' height='70'/>
