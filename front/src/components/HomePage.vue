<template>
    <div class="w-screen h-screen flex justify-center items-center "> 
     
      <div class="container mx-auto px-4 sm:px-8 py-12 sm:py-24 flex flex-col sm:flex-row items-center justify-between">
        <!-- Content Container -->
        <div class="max-w-lg sm:max-w-xl ml-12">
          <h1 class="text-3xl sm:text-3xl font-bold  mb-4 sm:mb-6">Welcome to Alzheimer's Disease Detection</h1>
          <p class="text-base sm:text-md text-gray-700 leading-relaxed">Early detection of Alzheimer's disease is crucial for effective management and treatment. Our innovative platform uses state-of-the-art machine learning technology to assist in the early diagnosis of Alzheimer's disease through brain image analysis.</p>
          
          <h2 class="text-xl sm:text-xl font-semibold mt-4 mb-2">How it Works:</h2>
          <ol class="list-decimal text-base sm:text-md text-gray-700 leading-relaxed ml-6">
            <li>Upload Your Brain Image: Simply upload a brain image using our user-friendly interface.</li>
            <li>Receive Predictions: Our advanced algorithms analyze the image to detect potential signs of Alzheimer's disease.</li>
            <li>Get Results: Within moments, you'll receive comprehensive results indicating the likelihood of Alzheimer's disease based on the uploaded image.</li>
          </ol>
          
          <button class="btn btn-primary mt-6 sm:mt-4 block w-full sm:w-auto ml-1/2 sm:mx-0 " @click="useToast.openModal=true">Start Prediction</button>
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
  
 