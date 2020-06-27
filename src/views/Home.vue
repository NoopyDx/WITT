<template>
  <div class="home text-center">
    <!-- DEBUG LINE <h1>{{ this.info.data.url }}</h1> -->
    <v-row style="margin:15px">
      <v-col cols="6">
        <v-img
          alt="Vuetify Logo"
          :src="this.info.data.url"
          transition="scale-transition"
          height="400px"
          contain
        />
      </v-col>

      <v-col align-self="stretch">
        <!-- <v-row justify="start" v-for="answer in info.data.answer" :key="answer" cols="6"> -->
        <div id="flex-system" class="container">
          <v-card
            v-for="answer in info.data.answer"
            :key="answer"
            :class="{ 'winAnimation': answered && answer==info.data.rep }"
            id="answer-card"
            :style="
            answered
              ?  answer == info.data.rep ? 'background-color:green;color:whitesmoke'
              : 'background-color: red; color :whitesmoke' : 'background-color: #fad390;'
          "
            @click="sendAnswer(answer)"
            :disabled="answered"
          >{{ answer }}</v-card>
        </div>

        <!-- </v-row> -->
      </v-col>
    </v-row>
    <v-btn
      v-if="answered"
      dark
      class="ma-2 btnStyle"
      rounded
      color="#60a3bc"
      onclick="location.reload(true)"
    >
      <v-icon left>mdi-chevron-right</v-icon>Suivant
    </v-btn>
    <!-- <v-row v-if="!answered" justify="center" align="center">
      <v-col v-for="answer in info.data.answer" :key="answer" cols="6">
        <v-card
          class="d-inline-block"
          id="answer-card"
          :style="
            answered && answer == info.data.rep
              ? 'background-color:green;color:whitesmoke'
              : 'background-color: #fad390;'
          "
          @click="sendAnswer(answer)"
          :disabled="answered"
          >{{ answer }}</v-card
        >
      </v-col>
    </v-row>-->
    <!-- <h3
      v-if="answered"
      :style="result ? 'color:green;' : 'color: #eb2f06;'"
      style="color:whitesmoke"
    >{{ this.textResult }}</h3>-->
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      info: null,
      result: null,
      answered: false,
      textResult: null
    };
  },
  components: {},
  methods: {
    sendAnswer: function(answer) {
      this.answered = true;
      if (answer == this.info.data.rep) {
        this.result = true;
        this.textResult = "Bonne réponse !";
      } else {
        this.result = false;
        this.textResult = "Pas du tout...";
      }
      // Using axios here
    },
    reloadPage() {
      window.location.reload();
    }
  },
  mounted() {
    axios.get("http://149.202.40.137:5000").then(response => {
      this.info = response;
    });
    console.log(this.info);
  }
};
</script>
<style scoped>
.normal-text {
  color: whitesmoke;
}

#answer-card {
  background-color: #2980b9;
  font-family: "Balsamiq Sans", cursive;
  text-align: center;
  color: #0c2461;
  font-weight: bold;
  font-size: 20px;
  padding: 5px;
}
#flex-system {
  display: flex;
  flex-direction: column-reverse;
  justify-content: space-between !important;
  height: 100%;
}

.btnStyle {
  font-weight: bold;
}

.winAnimation {
  animation-name: shake;
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-timing-function: ease-in;
}

@keyframes shake {
  0% {
    transform: rotate(1deg);
  }
  10% {
    transform: rotate(-1deg);
  }
  20% {
    transform: rotate(1deg);
  }
  30% {
    transform: rotate(-1deg);
  }
  40% {
    transform: rotate(1deg);
  }
  50% {
    transform: rotate(-1deg);
  }
  60% {
    transform: rotate(1deg);
  }
  70% {
    transform: rotate(-1deg);
  }
  80% {
    transform: rotate(1deg);
  }
  90% {
    transform: rotate(-1deg);
  }
  100% {
    transform: rotate(1deg);
  }
}
</style>
