# Seasonal-songs

## 프로젝트 주제
음원 사이트 "melon"의 봄/겨울에 흥행한 노래 시각화

#### 프로젝트 주제 선정 이유
음악은 계절과 감정, 상황에 따라 다양한 변화를 보입니다. 특히, 봄과 겨울은 각각 생명의 시작과 종말, 활기와 정적을 상징하는 계절로 알려져 있습니다. 이런 계절의 특성이 음악 선택에 어떠한 영향을 미치는지 알아보는 것이 이번 프로젝트의 첫 번째 목표입니다.
또한, 각 계절에 흥행한 곡들을 분석함으로써, 그 시기의 사회적 분위기나 트렌드를 엿볼 수 있습니다. 이를 통해 우리는 음악이 단순한 예술 형태를 넘어, 시대와 문화, 사람들의 감정을 반영하는 매개체라는 것을 확인할 수 있습니다.
따라서, 이번 프로젝트에서는 음원 사이트 'melon'에서 데이터를 수집하고, 봄/겨울에 흥행한 노래를 시각화하여, 이러한 목표를 달성하고자 했습니다.

## 활용 기술 및 프레임 워크, 배포 환경
![Untitled](https://github.com/4-2-teamproject/Seasonal-songs/assets/112957047/c14d145b-f675-473f-96c9-8ab196c372d8)

## 참여자
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/zjacom"><img src="https://avatars.githubusercontent.com/u/112957047?v=4" width="100px;" alt=""/><br /><sub><b>김승훈</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/taeyeon5362"><img src="https://avatars.githubusercontent.com/u/51779879?v=4" width="100px;" alt=""/><br /><sub><b>김태연</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/dldudwns887"><img src="https://avatars.githubusercontent.com/u/70689930?v=4" width="100px;" alt=""/><br /><sub><b>이영준</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/rehayoung"><img src="https://avatars.githubusercontent.com/u/119647020?v=4" width="100px;" alt=""/><br /><sub><b>이하영</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/SpaceSurfer051"><img src="https://avatars.githubusercontent.com/u/107080228?v=4" width="100px;" alt=""/><br /><sub><b>최수범</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>

## 역할 분담 및 역할 별 요구사항
### 데이터 수집 파트(이영준, 이영하)
#### 요구사항
- 2010년부터 2024년까지, 봄(03월,04월,05월),겨울(01월,02월,12일)를 순차적으로 조회
- 조회한 페이지의 TOP 100 chart 데이터를 스크랩
- 데이터 시각화를 위해, 각 조건에 맞는 데이터로 분화
### 백엔드 / 프론트엔드 파트(김승훈, 김태연, 최수범)
#### 요구사항
- 날짜별 차트 현황(꺾은선 그래프), 노래 리스트 시각화
- 년도별(2012~2023), 계절별(봄, 겨울) 페이지 구현
- 명예의 전당, 봄, 겨울 노래 총 개수, 노래 선정 기준을 시각화 할 수 있는 모달(modal) 구현

## 결과물
### 봄 메인 페이지
![spring_main](https://github.com/4-2-teamproject/Seasonal-songs/assets/112957047/f116f72d-0f64-421e-8f94-52b07196fa8b)
### 봄 모달
<img width="421" alt="spring_modal" src="https://github.com/4-2-teamproject/Seasonal-songs/assets/112957047/b1caae65-b517-45ad-ace6-57fca51c2068">

### 겨울 메인 페이지
![winter_main](https://github.com/zjacom/PS/assets/112957047/b0517f4b-0057-41c0-be29-5c425765c307)
### 겨울 모달
<img width="423" alt="winter_modal" src="https://github.com/4-2-teamproject/Seasonal-songs/assets/112957047/1f8e1039-29ed-4a98-8660-2b3604af028e">

## 기대효과
- 봄과 겨울 시즌에 어떤 노래가 흥행했는지에 대한 정보를 얻을 수 있고, 해당 정보를 바탕으로 계절(봄, 겨울) 별로 사람들이 어떤 음악을 선호하는지, 이러한 선호도가 몇 년에 걸쳐 나타나는지에 대한 이해를 도울 수 있다.
- 사람들이 체감하는 봄과 겨울을 실제 벚꽃 개화 시기와 첫눈이 내리는 시기와 대조하여 비교할 수 있다.
- 이러한 이해는 음악 산업에 관련된 사람들에게 유용한 정보를 제공할 수 있다.
  - 예를 들어 음악 프로듀서나 아티스트는 이 정보를 바탕으로 많은 사람들이 선호하는 음악의 느낌이 무엇인지, 곡을 만드는 데 도움이 될 수 있다.
  - 레코드 회사나 음악 유통업체는 이 정보를 활용하여 효과적인 마케팅 전략을 수립하는 데 좋은 의사결정 도구로 활용할 수 있을 것으로 추측된다.
