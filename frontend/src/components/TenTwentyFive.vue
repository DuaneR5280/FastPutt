<template>
    <v-container>
      <h1>1025 Game</h1>
  
      <v-card id="scorecard" class="mb-4">
        <v-card-text class="text-center">
          <div id="score-distance">{{ currentDistance }}</div>
          <v-card-subtitle>Feet</v-card-subtitle>
          <div id="score-score">{{ totalScore }}</div>
          <div id="score-station">{{ puttCount }} / 36</div>
          <v-card-subtitle>Putts</v-card-subtitle>
        </v-card-text>
      </v-card>
      <!-- Add in game stats div -->
      <v-container class="position-absolute bottom-0 left-0 right-0 w-100">
        <v-row justify="center">
          <v-col cols="12" sm="6" md="4">
            <v-text-field
              v-model="makesInput"
              type="number"
              hide-details
              hide-spin-buttons
              min="0"
              max="6"
              @focus="clearInput"
              class="centered-input"
            >
          <template v-slot:append>
            <v-icon color="green" @click="increment">
              mdi-plus
            </v-icon>
          </template>
          <template v-slot:prepend>
            <v-icon color="red" @click="decrement">
              mdi-minus
            </v-icon>
          </template>
          </v-text-field>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col cols="4">
            <v-btn 
              block
              :color="firstBtnClicked ? 'success' : 'secondary'"
              @click="recordFirst"
            >
              First
            </v-btn>
          </v-col>
          <v-col cols="4">
              <v-btn
                block
                :color="allBtnClicked ? 'success' : 'primary'"
                @click="recordAll"
              >
                All
              </v-btn>
          </v-col>
          <v-col cols="4">
              <v-btn
                block
                :color="lastBtnClicked ? 'success' : 'secondary'"
                @click="recordLast"
              >
                Last
              </v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            <v-btn block @click="undoMakes"><< Back</v-btn>
          </v-col>
  
          <v-col cols="6">
            <v-btn block @click="recordMakes">Next >></v-btn>
          </v-col>
        </v-row>
      </v-container>
  
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const distances = [10, 15, 20, 25, 30, 35];
  const currentDistanceIndex = ref(0);
  const currentDistance = ref(distances[currentDistanceIndex.value]);
  const totalScore = ref(0);
  const puttCount = ref(0);
  const puttsPerDistance = 6;
  const makesInput = ref(0);
  const firstPuttMade = ref(false);
  const lastPuttMade = ref(false);
  const allPuttMade = ref(false);
  const firstBtnClicked = ref(false);
  const lastBtnClicked = ref(false);
  const allBtnClicked = ref(false);
  
  const scoreHistory = ref({});

  const clearInput = () => {
  makesInput.value = '';
};
  
  const increment = () => {
    if (makesInput.value < 6) {
      makesInput.value++;
    }
  };

  const decrement = () => {
    if (makesInput.value > 0) {
      makesInput.value--;
    }
  };

  const recordAll = () => {
    makesInput.value = 6;
    firstPuttMade.value = true;
    lastPuttMade.value = true;
    allPuttMade.value = true;
    firstBtnClicked.value = true;
    lastBtnClicked.value = true;
    allBtnClicked.value = true;
  }

  const recordFirst = () => {
    firstPuttMade.value = !firstPuttMade.value;
    firstBtnClicked.value = !firstBtnClicked.value;
  }

  const recordLast = () => {
    lastPuttMade.value = !lastPuttMade.value;
    lastBtnClicked.value = !lastBtnClicked.value;
  }

  const recordMakes = () => {
    if (puttCount.value % puttsPerDistance === 0 && puttCount.value < 36) {
      puttCount.value += puttsPerDistance;  
      // Store current state in history
      scoreHistory.value[currentDistanceIndex.value] = {
        score: totalScore.value,
        puttCount: puttCount.value,
        makesInput: makesInput.value,
        firstPuttMade: firstPuttMade.value,
        lastPuttMade: lastPuttMade.value,
        allPuttMade: allPuttMade.value,
        firstBtnClicked: firstBtnClicked.value,
        lastBtnClicked: lastBtnClicked.value,
        allBtnClicked: allBtnClicked.value
      };
      
      const makes = parseInt(makesInput.value);
      const bonus = currentDistance.value >= 30 ? 10 : 5;
    
      totalScore.value += makes * currentDistance.value;
    
      if (firstPuttMade.value) {
        totalScore.value += bonus;
      }
      if (lastPuttMade.value) {
        totalScore.value += bonus;
      }
      if (allPuttMade.value) {
        totalScore.value += currentDistance.value;
      }
      
      nextStation();
    }
  };

  const undoMakes = () => {
    if (scoreHistory.value[currentDistanceIndex.value - 1]) {
      // Retrieve previous state from history
      const previousState = scoreHistory.value[currentDistanceIndex.value - 1];
      totalScore.value = previousState.score;
      puttCount.value = previousState.puttCount;
      makesInput.value = previousState.makesInput;
      firstPuttMade.value = previousState.firstPuttMade;
      lastPuttMade.value = previousState.lastPuttMade;
      allPuttMade.value = previousState.allPuttMade;
      firstBtnClicked.value = previousState.firstBtnClicked;
      lastBtnClicked.value = previousState.lastBtnClicked;
      allBtnClicked.value = previousState.allBtnClicked;

      delete scoreHistory.value[currentDistanceIndex.value -1];

      currentDistanceIndex.value--;
      currentDistance.value = distances[currentDistanceIndex.value];
    }
  };

  const nextStation = () => {
    currentDistanceIndex.value++;
    if (currentDistanceIndex.value < distances.length) {
      currentDistance.value = distances[currentDistanceIndex.value];
    }
    makesInput.value = 0;
    firstPuttMade.value = false;
    lastPuttMade.value = false;
    allPuttMade.value = false;
    firstBtnClicked.value = false;
    lastBtnClicked.value = false;
    allBtnClicked.value = false;
  };
  
  const resetGame = () => {
  currentDistanceIndex.value = 0;
  currentDistance.value = distances[currentDistanceIndex.value];
  totalScore.value = 0;
  puttCount.value = 0;
  makesInput.value = 0;
  firstPuttMade.value = false;
  lastPuttMade.value = false;
  allPuttMade.value = false;
  firstBtnClicked.value = false;
  lastBtnClicked.value = false;
  allBtnClicked.value = false;
  scoreHistory.value = {};
};
  </script>
<style scoped>
#scorecard {
  display: flex;
  align-items: center;
  justify-content: center;
}

#score-distance {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

#score-score {
  font-size: 10rem;
  font-weight: bold;
  color: #1976D2; /* Example primary color */
}

#score-station {
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.centered-input >>> input{
  text-align: center;
}

@media (max-width: 600px) {
  #score-distance {
    font-size: 1.2rem;
  }

  #score-score {
    font-size: 3rem;
  }

  #score-station {
    font-size: 1rem;
  }
}
</style>