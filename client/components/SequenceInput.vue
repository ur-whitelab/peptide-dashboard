<template>
  <input id="sequence" class="input" spellcheck="false"
  autocorrect="off" type="text" placeholder="Peptide Sequence"
  v-model="internalSequence" @keydown="onKeyDown">
</template>

<script>
// https://stackoverflow.com/questions/46289311/vue-limit-characters-in-text-area-input-truncate-filter
export default {
  name: 'SequenceInput',
  data () {
    return {
      sequence: '',
      pattern: 'acdefghiklmnpqrstvwyACDEFGHIKLMNPQRSTVWY'
    }
  },
  mounted: function () {
    // convert pattern to list of integers
    this.pattern = this.pattern.split('').map((x) => { return x.charCodeAt(0) })
  },
  computed: {
    internalSequence: {
      get: function () { return this.sequence },
      set: function (v) {
        this.sequence = v
        this.$emit('sequence-update', v)
      }

    }
  },
  methods: {
    onKeyDown: function (evt) {
      // do this instead of rex so it's faster
      // check if it's a control character
      if (evt.keyCode >= 48 && evt.keyCode <= 90) {
        if (this.pattern.indexOf(evt.keyCode) < 0)
          evt.preventDefault()
      }
    }
  }
}
</script>

<style lang="scss">
@import "style/style.scss";
#sequence {
  font-family: $family-mono;
  text-transform: uppercase;
}
</style>
