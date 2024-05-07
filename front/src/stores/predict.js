import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const usePredictionStore = defineStore('prediction', () => {
  const ImageToPredict = ref(null)
const PredictedResults=ref(null)
  // Function to send image for prediction
  const predictImage = async () => {
    try {
      if (ImageToPredict.value) {
        const formData = new FormData()
        formData.append('file', ImageToPredict.value)

        const response = await fetch('http://localhost:8000/predict/', {
          method: 'POST',
          body: formData
        })

        if (response.ok) {
          const result = await response.json()
          // Handle the prediction result here
          console.log('Prediction result:', result)
          PredictedResults.value=result
        } else {
          console.error('Failed to get prediction:', response.statusText)
        }
      } else {
        console.error('No image selected for prediction')
      }
    } catch (error) {
      console.error('Error predicting:', error)
    }
  }

  return { ImageToPredict, predictImage ,PredictedResults}
})

