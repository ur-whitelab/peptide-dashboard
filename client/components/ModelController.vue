<template>
  <div>
    <h4>
      Training
      <span v-if="training"> In Progress {{progress}}</span>
      <span v-else> Stopped</span>
    </h4>
     <button v-on:click="startTrain">Start</button>
     <button v-on:click="stopTrain">Stop</button>
     <button v-on:click="deleteTrain">Delete</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'model-controller',
  props: {
    port: {
      default: '5000',
      type: String
    },
    host: {
      default: 'localhost',
      type: String
    },
    updateFrequency: {
      default: 1000,
      type: Number
    }
  },
  data () {
    return {
      progress: '0',
      training: false
    }
  },
  methods: {
    startTrain: async function () {
      try {
        const response = await axios.get(
          'http://' + this.host + ':' + this.port + '/train/start'
        )
        if ('status' in response.data)
          this.progress = response.data.status
        this.training = true
        await this.updateProgress()
      } catch (err) {
        // pass
      }
    },
    stopTrain: async function () {
      try {
        const response = await axios.get(
          'http://' + this.host + ':' + this.port + '/train/stop'
        )
        if ('status' in response.data)
          this.progress = response.data.status
        this.training = false
      } catch (err) {
        // pass
      }
    },
    deleteTrain: async function () {
      await this.stopTrain()
      try {
        await axios.get('http://' + this.host + ':' + this.port + '/train/delete')
      } catch (err) {
        // pass
      }
    },
    updateProgress: async function () {
      try {
        const response = await axios.get('http://' + this.host + ':' + this.port + '/train/status')
        if ('status' in response.data)
          this.progress = response.data.status
      } catch (err) {
        // pass
      } finally {
        if (this.training)
          setTimeout(this.updateProgress, this.updateFrequency)
      }
    }
  }
}
</script>