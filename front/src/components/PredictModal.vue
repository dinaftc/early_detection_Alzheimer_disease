<template>
  <input type="checkbox" id="openModal" :checked="useToast.openModal" class="modal-toggle" />
  <div class="modal modal-middle" role="dialog">
    <div class="modal-box w-full sm:w-96 xs:max-w-sm h-2/3 md:h-2/3 overflow-hidden relative">
      <plus-icon class="rotate-45 h-6 w-6 absolute top-6 left-80 fill-secondary" @click="useToast.openModal=false"/>
      <div class="form-control w-full sm:w-80 flex flex-col items-center justify-center mx-auto">
        <label class="label my-4">
          <span class="pixa-title text-lg font-semibold">Upload Your Brain Image</span>
        </label>
        <div class="w-80 h-48 rounded-md border-dashed border-2 border-gray-300 relative flex items-center justify-center overflow-hidden">
          <input type="file" @change="handleRectoChange" accept="application/pdf, image/png, image/jpeg" class="opacity-0 absolute inset-0 z-10 cursor-pointer">
          <plus-icon class="w-6 h-6 absolute" v-if="!tempIdentityRecto"/>
          <img v-if="tempIdentityRecto" :src="tempIdentityRecto" class="object-cover w-full h-full rounded" alt="">
        </div>
        <button class="btn btn-primary mt-6 sm:mt-8 block w-full sm:w-auto mx-auto sm:mx-0" @click="usePrediction.predictImage">Predict Now</button>
        <label class="label gap-2 my-4 text-accent" v-if="usePrediction.PredictedResults">
          <span class=" text-lg font-semibold text-accent">Results:</span>
          <p class="text-base label-text">{{ usePrediction.PredictedResults }}</p>
        </label>
      </div> 
    </div>
  </div>
  
</template>
<script setup>
import { useToastStore } from '@/stores/toast';
import { ref } from 'vue';
import plusIcon from '@/assets/icons/plusIcon.vue';
import {usePredictionStore} from '@/stores/predict'
const useToast = useToastStore();
const tempIdentityRecto = ref(null);
const fileImage = ref(null);

const usePrediction=usePredictionStore()

const handleRectoChange = (event) => {
  const selectedFile = event.target.files[0];
  if (selectedFile) {
    fileImage.value = selectedFile;
    usePrediction.ImageToPredict=fileImage.value
    console.log(usePrediction.ImageToPredict)
    const reader = new FileReader();
    reader.onload = () => {
      tempIdentityRecto.value = reader.result;
    };
    reader.readAsDataURL(selectedFile);
  }
};
</script>
