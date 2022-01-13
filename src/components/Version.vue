<template>
  <div v-if="show" class="container">
    <article class="message is-warning">
      <div class="message-header">
        <p>This is science in progress!</p>
        <button
          @click="show = false"
          class="delete"
          aria-label="delete"
        ></button>
      </div>
      <div class="message-body">
        <strong> Version: {{ version }}</strong> You are viewing an early
        version of an upcoming research paper. The models and predictions shown
        here should be viewed for entertainment purposes only. Come back often
        for newer versions.
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