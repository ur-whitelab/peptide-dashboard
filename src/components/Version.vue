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
        are still being improved. Please see our 
        <a herf="https://www.biorxiv.org/content/10.1101/2022.05.18.492545v2"> our preprint</a> for more details 
        on the models and results.
        See the source code, open an issue if see a problem,
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
