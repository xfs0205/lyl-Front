import { ref } from "vue";
import { defineStore } from "pinia";
import {
  lazyAMapApiLoaderInstance,
  useCitySearch,
  useWeather,
} from "@vuemap/vue-amap";

export const useLocalCity = defineStore("useLocalCity", () => {
  const cityData = ref({
    data: null ,
    weather: null ,
  });
  const isLoading = ref(false);
  const isError = ref(false);

  async function getLocalCityData() {
    isLoading.value = true; // 开始加载时设置为 true
    isError.value = false;
    lazyAMapApiLoaderInstance
      .then(() => {
        useCitySearch()
          .then((res) => {
            const { getLocalCity } = res;
            return getLocalCity();
          })
          .then((cityResult) => {
            console.log("cityResult: ", cityResult);
            cityData.value.data = cityResult;
            return useWeather();
          })
          .then((resp) => {
            const { getForecast } = resp;
            return getForecast(cityData.value.data.city);
          })
          .then((forecastResult) => {
            console.log("forecastResult: ", forecastResult);
            cityData.value.weather = forecastResult;
            isLoading.value = true;
          })
          .catch((error) => {
            console.error("An error occurred:", error);
            isError.value = true;
          });
      })
      .catch((error) => {
        console.error("An error occurred with the API loader:", error);
        isError.value = true;
      });
  }

  return { cityData, isLoading, isError, getLocalCityData };
});
