<template>
  <div>
    <h4 class="is-size-4">Model Card</h4>
    <div class="tabs is-boxed">
      <ul>
        <template v-for="item in details" :key="item.id">
          <li :class="item.class">
            <a :id="'a-' + item.id" @click="tabUpdate">{{ item.name }}</a>
          </li>
        </template>
      </ul>
    </div>
    <p>
      {{ content }}
    </p>
  </div>
</template>
<style scoped>
.tabs ul {
  width: 100%;
  flex-direction: row;
  flex-wrap: wrap;
}
.tabs li {
  width: 50%;
}
</style>

<script>
export default {
  name: "ModelCard",
  props: {
    url: String,
  },
  data() {
    return {
      index: "title",
      card: null,
      title: "",
      details: [
        { id: "details", name: "Model Details", class: "is-active" },
        { id: "use", name: "Intended Use", class: "" },
        { id: "factors", name: "Factors", class: "" },
        { id: "metrics", name: "Metrics", class: "" },
        { id: "evaluation", name: "Evaluation Data", class: "" },
        { id: "training", name: "Training Data", class: "" },
        { id: "ethics", name: "Ethical Considerations", class: "" },
        { id: "caveats", name: "Caveats", class: "" },
      ],
      content: null,
    };
  },
  mounted: function () {
    fetch(this.url)
      .then((res) => res.json())
      .then((out) => {
        this.card = out;
        this.title = this.card["title"];
        this.content = this.card[this.details[0].id];
      });
  },
  methods: {
    tabUpdate(event) {
      const id = event.target.id.split("a-")[1];
      const new_details = this.details.map((v) => {
        v.class = "";
        if (v.id == id) v.class = "is-active";
        return { ...v };
      });
      this.details = new_details;
      this.content = this.card[id];
    },
  },
};
</script>
