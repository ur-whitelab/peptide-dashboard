<template>
  <div>
    <linked-input-box port="5000"></linked-input-box>
    <br/>
    <!-- v-bind to make a number -->
    <model-controller port="5000" v-bind:updateFrequency="100"></model-controller>
  </div>
</template>

<script>
  import LinkedInputBox from './LinkedInputBox'
  import ModelController from './ModelController'

  export default {
    name: 'App',
    components: {LinkedInputBox, ModelController}
  }
</script>

<style>
  @import "~bulma/bulma.sass";
</style>
