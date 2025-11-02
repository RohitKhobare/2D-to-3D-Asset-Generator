// we've imported the @trainorpj/sentiment library
const { scaleThreshold, scaleOrdinal } = d3;

const analyze = phrase => {
  const val = sentiment(phrase);
  return {
    comparative: val.comparative,
    negative: val.negative,
    positive: val.positive
  };
};

const emojis = ["😍", "🙂", "😑", "🙁", "😠"];
const colors = ["#2979FF", "#81D4FA", "#EDE7F6", "#F48FB1", "#E53935"];

const emojiColor = scaleOrdinal()
  .domain(emojis)
  .range(colors);

const emojiSentiment = scaleThreshold()
  .domain([-3, -1, 1, 3, 5])
  .range([...emojis].reverse());

var app = new Vue({
  el: "#app",
  data() {
    return {
      emojis,
      phrase: ``
    };
  },
  computed: {
    analysis: function() {
      const { comparative, positive, negative } = sentiment(this.phrase);
      return {
        comparative: comparative.toFixed(2),
        positive,
        negative
      };
    },
    bgc: function() {
      const emoji = emojiSentiment(this.analysis.comparative);
      const color = emojiColor(emoji);
      return { backgroundColor: color }
    }
  },
  methods: {
    changeBgc(val) {
      const emoji = emojiSentiment(val);
      const color = emojiColor(emoji);
      this.bgc.backgroundColor = color;
    },
    getBgc(emj) {
      return emojiColor(emj);
    }
  }
});