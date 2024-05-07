<template>
  <div 
    class="w-full h-screen flex justify-center overflow-hidden ">
    <div class="w-full h-full overflow-auto">
      <div class="w-full h-fit flex flex-col ">
        <div class="w-full h-screen relative flex justify-center">
          <div class="w-full h-full overflow-hidden relative ">   
          <div class="w-full h-fit max-w-screen-3xl absolute px-8 flex flex-col items-center ">
            <top-navigation />
          </div>
          <home-page/>
   
        </div>
      
        </div>
       
      </div>
    </div>
  </div>
</template>

<script setup>
import topNavigation from '@/components/topNavigation.vue';
import HomePage from '@/components/HomePage.vue'

</script>
