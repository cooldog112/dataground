import streamlit as st

st.header("데이터 전처리란?")
st.write("데이터 전처리는 데이터 분석의 첫 번째 단계로 데이터 분석이나 모델링을 하기 전에 데이터를 정리하고 가공하는 과정이다.")
st.write("데이터 분석에 사용된 데이터에 오류가 있다면 분석 결과의 신뢰성은 떨어질 것이다.")
st.write("데이터 전처리를 통해 데이터의 오류를 수정하거나 데이터를 분석하기 용이하게 수정할 수 있다.")

st.header("데이터 전처리의 주요 단계")
st.subheader("1. 데이터 필터링")
st.write("데이터를 분석하기 적합한 상태로 만들기 위해 필요한 데이터만 선택하고 불필요한 데이터를 제거하는 단계")
st.write("분석하려는 기간의 데이터만 추출하거나 특정 조건에 부학하는 데이터만 추출하는 경우에 해당된다.")
st.subheader("2. 결측값 처리")
st.write("데이터셋에서 누락된 값이 있을 때 이를 처리하는 과정이다. 결측값이 있는 데이터를 그대로 사용하면 분석 결과가 왜곡될 수 있다.")
st.error("삭제 : 결측값이나 포함된 행이나 열을 제거한다.")
st.success('대체 : 결측값을 평균, 중앙값 또는 다른 추정값으로 대체한다.')
st.subheader("3. 이상치 탐지 및 처리")
st.write("이상치는 데이터에서 다른 값들과 크게 벗어나는 비정상적인 데이터를 의미한다. 이러한 값은 분석에 악영향을 미칠 수 있기 때문에 전처리 단계에서 이상치를 확인하고 처리해야한다. 결측값과 마찬가지로 이상치를 삭제하거나 대체한다.")

st.subheader("4. 데이터 전처리의 중요성")
st.write(" - 데이터 전처리는 잘못된 데이터를 정제함으로써 정확한 결과를 도출할 수 있게 해준다.")
st.write(" - 머신러닝을 학습시킬 때 정제된 데이터를 제공하면 모델의 성능이 크게 향상된다.")
st.write(" - 분석 과정에서 발생할 수 있는 오류를 줄여준다.")