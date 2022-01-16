<template>
  <div v-if="show" class="container">
    <article class="message is-info">
      <div class="message-header">
        <p>Important Note</p>
        <button
          @click="show = false"
          class="delete"
          aria-label="delete"
        ></button>
      </div>
      <div class="message-body has-text-dark">
        <strong> v{{ version }}</strong> You are viewing an early version of
        ongoing research. The predictions shown here are based on models that
        are still being improved. I have made this accessible to gather feedback
        and engage other experts in peptide chemistry. Please come back often
        for newer versions. See the source code, open an issue if see a problem,
        and watch the
        <a href="https://github.com/ur-whitelab/peptide-dashboard"
          >github repo</a
        >
        to stay updated on new versions.
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: "Version",
  props: {
    version: String,
  },
  data() {
    return {
      show: true,
    };
  },
};
</script>