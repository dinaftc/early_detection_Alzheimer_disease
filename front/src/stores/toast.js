import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useToastStore = defineStore('toast', () => {
  const toast = ref({
    show: false,
    message: '',
    type: ''
  })
 
  const openModal = ref(false)
 
 
  
  const openToast = (showToast, messageToast, typeToast) => {
    if (showToast) {
      toast.value.message = messageToast
      toast.value.type = typeToast
      toast.value.show = true
      setTimeout(() => {
        closeToast()
      }, 2000)
    } else {
      closeToast()
    }
  }


  
  const closeToast = () => {
    toast.value.show = false
    setTimeout(() => {
      toast.value.message = ''
      toast.value.type = ''
    }, 1000)
  }

  return {
    toast,
    openToast,
    closeToast,
    openModal
  }
})
