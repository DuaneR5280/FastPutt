<template>

  <v-container fill-height d-flex flex-column>
    <h1>Circle 1</h1>

    <v-card id="scorecard" v-if="!roundOver">
      <v-card-text class="text-center">
        <div id="score-distance">{{ currentDistance }}</div>
        <v-card-subtitle>Feet</v-card-subtitle>
        <div id="score-score">{{ roundTotalMakes }}</div>
        <div id="score-station">{{ currentDistanceIndex + 1 }} / {{ distances.length }}</div>
        <v-card-subtitle>station</v-card-subtitle>
        <div id="makes-percent">{{ currentMakePercentage }}</div>
      </v-card-text>
    </v-card>

    <v-container v-if="!roundOver" justify="center" class="position-absolute bottom-0 left-0 right-0 w-100">
      <v-row class="d-flex justify-space-between">
        <v-col v-for="value in firstRowValues" :key="value" cols="2">
          <v-btn
            block
            :color="clickedValue === value ? 'success' : 'primary'"
            @click="recordMakes(value)">
            {{ value }}
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-space-between">
        <v-col v-for="value in secondRowValues" :key="value" cols="2">
          <v-btn
            block
            :color="clickedValue === value ? 'success' : 'primary'"
            @click="recordMakes(value)">
            {{ value }}
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="d-flex justify-space-between">
        <v-col cols="12">
        <v-btn
          block
          :color="clickedValue === 10 ? 'success' : 'primary'"
          @click="recordMakes(10)">
          10
        </v-btn>
        </v-col>

      </v-row>
      <v-row>
        <v-col cols="6">
          <v-btn block @click="previousStation" :disabled="currentDistanceIndex === 0">
            &lt;&lt; back
          </v-btn>
        </v-col>
        <v-col cols="6">
          <v-btn block @click="nextStation" :disabled="currentDistanceIndex === distances.length - 1">
            next &gt;&gt;
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <div v-if="currentDistanceIndex === distances.length - 1 && roundOver && !gameOver" class="mt-4">
      <h2>Round Results</h2>

      <div>
        <h3>Round {{ roundIdCounter }}</h3>
        <v-table>
          <thead>
            <tr>
              <th class="text-left">Distance</th>
              <th class="text-left">Makes</th>
              <th class="text-left">Make %</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(station, stationIndex) in roundStations" :key="stationIndex">
              <td>{{ station.distance }}</td>
              <td>{{ station.makes }}</td>
              <td>{{ calcMakePercentage(station.makes, station.attempts) }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td>Round Total</td>
              <td>{{ roundTotalMakes }}</td>
              <td>{{  calcMakePercentage(roundTotalMakes, roundTotalAttempts) }}</td>
            </tr>
          </tfoot>
        </v-table>
      </div>
    </div>

      <div id="stats" v-if="gameOver">
        <h3>Session Stats</h3>
        <v-row>
          <v-col
            block
          >            
            Date: {{ gameStart }}
          </v-col>
          <v-col block>
            Time: {{ gameTime }}
          </v-col>
          <v-col block>
            Duration: {{ gameDuration }}
          </v-col>
        </v-row>
        <v-text-field v-model="conditions" label="Conditions" />
        <v-textarea v-model="notes" label="Notes" />

        <v-row>
          <v-col
            block
            cols="4">
            Total Makes: {{ gameTotalMakes }}
          </v-col>
          <v-col block cols="4">
            Total Attempts: {{ gameTotalAttempts }}
          </v-col>
          <v-col block cols="4">
            Overall Makes: {{ calculateSessionPercentage() }}
          </v-col>
        </v-row>
        
        <div v-for="(round, roundIndex) in rounds" :key="roundIndex">
          <h3>Round {{ round.roundId }}</h3>
          <v-table>
            <thead>
              <tr>
                <th class="text-left">Distance</th>
                <th class="text-left">Makes</th>
                <th class="text-left">Make %</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(station, stationIndex) in round.stations" :key="stationIndex">
                <td>{{ station.distance }}</td>
                <td>{{ station.makes }}</td>
                <td>{{ calcMakePercentage(station.makes, station.attempts) }}</td>
              </tr>
            </tbody>

            <tfoot>
              <tr>
                <td>Round Total</td>
                <td>{{ round.roundTotalMakes }}</td>
                <td>{{  calcMakePercentage(round.roundTotalMakes, round.roundTotalAttempts) }}</td>
              </tr>
            </tfoot>
          </v-table>
        </div>
        <v-btn
          block
          :color="clickedValue === 'saved' ? 'success' : 'primary'"
          class="mt-4"
          @click="saveGame">
          Save Game
        </v-btn>
      </div> <!-- stats -->
      <div id="stats" v-if="roundOver && !gameOver">
        <v-row>
          <v-col>
            <v-btn block cols="6" class="mt-4" @click="playAgain">Play Again</v-btn>
          </v-col>
          <v-col>
            <v-btn block cols="6" class="mt-4" @click="endGame">End Game</v-btn>
          </v-col>
        </v-row>
      </div>


  </v-container>
</template>

<script setup>
import {v4 as uuidv4} from 'uuid';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();

// Game State
const gameStart = ref(new Date().toISOString());
const gameEnd = ref(null);
const gameDuration = ref(0);
const gameOver = ref(false);
const roundOver = ref(false);

// Game Data
const gameRules = ref('C1');
const conditions = ref('');
const notes = ref('');
const rounds = ref([]);
const gameTotalMakes = ref(0);
const gameTotalAttempts = ref(0)

// Round Data
const roundIdCounter = ref(1);
const roundStart = ref(new Date().toISOString());
const roundEnd = ref(null);
const roundDuration = ref(0);
const roundTotalMakes = ref(0);
const roundTotalAttempts = ref(0);
const roundStations = ref([]);

// Station Data
const distances = [15, 20, 25, 30, 35];
const currentDistanceIndex = ref(0);
const currentDistance = ref(distances[currentDistanceIndex.value]);
const attempts = ref(10);
const makesInput = ref(0);
const currentMakePercentage = ref(0);
const stationData = ref({});

// Scoring buttons
const buttonValues = ref([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
const firstRowValues = ref(buttonValues.value.slice(0, 5));
const secondRowValues = ref(buttonValues.value.slice(5, 10));
const clickedValue = ref(-1);  // Init to -1 to indicate no button has been clicked


const recordMakes = (value) => {
  clickedValue.value = value;
  const previousMakes = stationData.value[currentDistanceIndex.value] ? stationData.value[currentDistanceIndex.value].makes : 0;
  makesInput.value = value;

  stationData.value[currentDistanceIndex.value] = {
    distance: currentDistance.value,
    makes: makesInput.value,
    attempts: attempts.value,
  };

  updateScore(previousMakes);
  
  if (currentDistanceIndex.value === distances.length - 1) {
    roundStations.value = (Object.values(stationData.value));
    roundOver.value = true;
  }
};

const updateScore = (previousMakes) => {
  roundTotalMakes.value += makesInput.value - previousMakes;

  if (Object.keys(stationData.value).length > 0) {
    roundTotalAttempts.value = Object.values(stationData.value).length * attempts.value;
  }

  if (roundTotalAttempts.value > 0) {
    currentMakePercentage.value = ((roundTotalMakes.value / roundTotalAttempts.value) * 100).toFixed(2);
  } else {
    currentMakePercentage.value = 0;
  }
};

const nextStation = () => {
  if (currentDistanceIndex.value < distances.length - 1 && clickedValue.value !== -1) {
    currentDistanceIndex.value++;
    currentDistance.value = distances[currentDistanceIndex.value];
    if (stationData.value[currentDistanceIndex.value]) {
      clickedValue.value = stationData.value[currentDistanceIndex.value].makes;
      makesInput.value = stationData.value[currentDistanceIndex.value].makes;
    } else {
      clickedValue.value = -1;
      makesInput.value = 0;
    }
  }
  else {
    alert('Record makes before moving to the next station.');
  }
};

const previousStation = () => {
  if (currentDistanceIndex.value > 0) {
    currentDistanceIndex.value--;
    currentDistance.value = distances[currentDistanceIndex.value];
    makesInput.value = stationData.value[currentDistanceIndex.value].makes;
    clickedValue.value = makesInput.value;
  }
};

const calcMakePercentage = (makes, attempts) => {
  if (attempts === 0) {
    return '0%';
  }
  return ((makes / attempts) * 100).toFixed(2) + '%';
}

const endGame = () => {
  roundOver.value = true;
  gameOver.value = true;
  endRound();
  // Needs to redirect to finish page where conditions and notes can be entered before submitting
  gameEnd.value = new Date().toISOString();
  gameDuration.value = (new Date(gameEnd.value) - new Date(gameStart.value)) / 1000;
};

const saveGame = async () => {
    clickedValue.value = 'saved';
    const gameResult = {
        gameStart: typeof gameStart.value === 'string' ? gameStart.value : new Date(gameStart.value).toISOString(),
        gameEnd: typeof gameEnd.value === 'string' ? gameEnd.value : (gameEnd.value ? new Date(gameEnd.value).toISOString() : null),
        gameDuration: gameDuration.value,
        gameRules: gameRules.value,
        conditions: conditions.value,
        notes: notes.value,
        rounds: rounds.value,
        totalMakes: gameTotalMakes.value,
        totalAttempts: gameTotalAttempts.value
    };

    try {
        console.log('Sending game data:', JSON.stringify(gameResult, null, 2));  // Debug log
        const response = await axios.post('/api/games/', gameResult);
        console.log('Response:', response.data);  // Debug log
        const gameId = response.data.uuid;
        if (gameId) {
            router.push(`/games/${gameId}`);
        } else {
            alert('Game saved, but no game ID returned.');
        }
    } catch (error) {
        console.error('Full error:', error);  // Enhanced error logging
        console.error('Error response:', error.response);  // Show response if available
        alert('Failed to save game. Please try again.');
    }
};

const playAgain = () => {
  endRound();
  resetGame();
};

const endRound = () => {
  roundEnd.value = new Date().toISOString();
  roundDuration.value = (new Date(roundEnd.value) - new Date(roundStart.value)) / 1000;
  updateGameStats();

  rounds.value.push(
    {
      roundId: roundIdCounter.value,
      roundStart: typeof roundStart.value === 'string' ? roundStart.value : new Date(roundStart.value).toISOString(),
      roundEnd: typeof roundEnd.value === 'string' ? roundEnd.value : new Date(roundEnd.value).toISOString(),
      roundDuration: roundDuration.value,
      roundTotalMakes: roundTotalMakes.value,
      roundTotalAttempts: roundTotalAttempts.value,
      stations: roundStations.value
    }
  );

  if (!gameOver.value) {
    roundIdCounter.value++;
  }

}

const resetGame = () => {
  currentDistanceIndex.value = 0;
  currentDistance.value = distances[0];
  roundTotalMakes.value = 0;
  roundTotalAttempts.value = 0;
  makesInput.value = 0;
  clickedValue.value = -1;
  currentMakePercentage.value = 0;
  stationData.value = {};
  roundStations.value = [];
  roundOver.value = false;
  roundStart.value = new Date().toISOString();
  roundEnd.value = null;
};


const updateGameStats = () => {
  gameTotalMakes.value += roundTotalMakes.value;
  gameTotalAttempts.value += roundTotalAttempts.value;
};

const calculateSessionPercentage = () => {
  if (gameTotalAttempts.value === 0) {
    return '0%';
  }
  return ((gameTotalMakes.value / gameTotalAttempts.value) * 100).toFixed(2) + '%';
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
  color: #1976D2;
  /* Example primary color */
}

#score-station {
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.centered-input>>>input {
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