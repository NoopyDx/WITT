<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12" style>
        <div class="main-title2">
          <div class="main-title">C'est quoi ce machin ?!</div>
        </div>
        <div class="sourceFont">Source : Reddit.com - r/whatisthisthing</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld"
};
</script>

<style scoped>
.main-title {
  align-content: center;
  font-family: "Roboto", sans-serif;
  font-size: 40px;
  color: white;
  /* border: 5px white inset; */
  border-radius: 11px;
  width: 500px;
  text-align: center;
  display: inline-block;
  padding: 1%;
  position: relative;
}

.main-title::after {
  content: "";
  display: block;
  position: absolute;
  width: 85px;
  height: 50px;
  top: 0px;
  left: 0px;
  border-left: 3px solid white;
  border-top: 3px solid white;
  border-radius: 11px 0 0 0;
  /* #2c3e50 */
}
.main-title::before {
  content: "";
  display: block;
  position: absolute;
  width: 85px;
  height: 50px;
  top: 35px;
  left: 410px;
  border-right: 3px solid white;
  border-bottom: 3px solid white;
  border-radius: 0 0 11px 0;
  /* #2c3e50 */
}

.sourceFont {
  font-family: "Pangolin", cursive;
  color: #f8c291;
  font-size: 2 px;
  margin-bottom: -10px;
}
</style>
