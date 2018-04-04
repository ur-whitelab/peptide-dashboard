<template>
  <canvas ref="sequenceGraph" width="960" height="450"> </canvas>
</template>

<script>
import SequenceD3 from './lib/sequence.js'
import _ from 'lodash'
export default {
  name: 'SequenceViewer',
  props: {
    sequence: String
  },
  data () {
    return {
      sd3: null
    }
  },
  mounted: function () {
    this.sd3 = new SequenceD3(this.$refs.sequenceGraph)
  },
  watch: {
    sequence: _.debounce(function () {
      this.sd3.update(this.sequence)
    }, 250)

  }
}
</script>

<style lang="scss">


</style>
