<template>
    <div class="w-screen h-screen flex justify-center items-center "> 
     
      <div class="container mx-auto px-4 sm:px-8 py-12 sm:py-24 flex flex-col sm:flex-row items-center justify-between">
        <!-- Content Container -->
        <div class="max-w-lg sm:max-w-xl ml-12">
          <h1 class="text-3xl sm:text-3xl font-bold  mb-4 sm:mb-6">Welcome to Alzheimer's Disease Detection</h1>
          <p class="text-md  text-gray-700 leading-relaxed">Early detection of Alzheimer's disease is crucial for effective management and treatment. Our innovative platform uses state-of-the-art machine learning technology to assist in the early diagnosis of Alzheimer's disease through brain image analysis.</p>
          
         
          <button class="btn btn-primary mt-8 sm:mt-6 block w-full sm:w-auto ml-1/2 sm:mx-0 " @click="useToast.openModal=true">Start Prediction</button>
        </div>
        
        <!-- Image Container -->
        <div class="w-full sm:w-1/2 max-w-xl sm:max-w-none mt-8 sm:mt-0">
          <img :src="bkg" alt="Alzheimer's Detection" class="w-full h-auto mx-auto sm:mx-0 ">
         </div>
      </div>
      <predict-modal/>
    </div>
  </template>
  
  <script setup>
    import bkg from '@/assets/images/natural-language-processing.jpg'
    import { useToastStore } from '@/stores/toast';
    import PredictModal from './PredictModal.vue';
    const useToast = useToastStore()
  </script>
  
 