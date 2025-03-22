<template>
  <v-container v-if="gameData">
    <h1>Game Summary {{ formatDate(gameData.gameStart).split(" ")[0] }}</h1>
    <v-subheader class="text-caption text-grey-lighten-1 mb-2">{{ gameId }}</v-subheader>
    <v-row>
      <v-col cols="4">
        <v-card
        class="mb-4"
        prepend-icon="mdi-clock"
        subtitle=""
        title="Start"
      >
        <v-card-text class="text-h4">{{ formatDate(gameData.gameStart).split(" ")[1] }}
        </v-card-text>
      </v-card>

      </v-col>
      <v-col cols="4">
        <v-card
          prepend-icon="mdi-timer"
          title="Duration">
          <v-card-text class="text-h4">
            {{ formatDuration(gameData.gameDuration) }}
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="4">
        <v-card
        class="mb-4"
        prepend-icon="mdi-clock"
        subtitle=""
        title="End"
      >
        <v-card-text class="text-h4">{{ formatDate(gameData.gameEnd).split(" ")[1] }}
        </v-card-text>
      </v-card>

      </v-col>      
    </v-row>

    <v-card prepend-icon="mdi-target" title="Total Putts" class="mb-4">
    <v-col>
      <v-card-text class="text-h1">
        {{ gameData.gameData.gameTotalMakes }} / {{ gameData.gameData.gameTotalAttempts }}
      </v-card-text>
      <v-progress-linear
        :model-value="totalMakePercentage"
        height="25"
        :color="getPercentageColor(totalMakePercentage)"
        rounded
      >
        <template v-slot:default="{ value }">
          <strong>{{ Math.round(value) }}%</strong>
        </template>
      </v-progress-linear>
    </v-col>
  </v-card>

    <!-- Progress Circles Stats -->
    <v-row>
      <v-col cols="4">
        <v-card
        class="mb-4"
        prepend-icon="mdi-check-bold"
        subtitle="session"
        title="C1 Goal"
      >
      <div class="d-flex justify-center align-center">
      <v-progress-circular
                :model-value=totalMakePercentage
                :rotate="-90"
                :size="100"
                :width="15"
                :color="getPercentageColor(totalMakePercentage)"
                >
                {{ totalMakePercentage }} %
              </v-progress-circular>
      </div>
      </v-card>
      </v-col>
      <v-col cols="4">
        <v-card
        class="mb-4"
        prepend-icon="mdi-cancel"
        subtitle="500 putts daily"
        title="Daily Goal"
      >
      <!-- Daily attempts goal ie: 500 putts a day -->
      <div class="d-flex justify-center align-center">
      <v-progress-circular
                :model-value=20
                :rotate="-90"
                :size="100"
                :width="15"
                :color="getPercentageColor(20)"
                >
                20 %
              </v-progress-circular>
      </div>
      </v-card>
      </v-col>
      <v-col cols="4">
        <v-card
        class="mb-4"
        prepend-icon="mdi-check-bold"
        subtitle="session"
        title="C2 Goal"
      >
      <div class="d-flex justify-center align-center">
      <v-progress-circular
                :model-value=totalMakePercentage
                :rotate="-90"
                :size="100"
                :width="15"
                :color="getPercentageColor(totalMakePercentage)"
                >
                {{ totalMakePercentage }} %
              </v-progress-circular>
      </div>
      </v-card>
      </v-col>

    </v-row>

    <v-card class="mb-4" v-if="gameData.gameData.conditions">
      <v-card-title>
        <h2>Conditions</h2>
      </v-card-title>
      <v-card-text>
        {{ gameData.gameData.conditions }}
      </v-card-text>
    </v-card>

    <v-card class="mb-4" v-if="gameData.gameData.notes">
      <v-card-title>
        <h2>Notes</h2>
      </v-card-title>
      <v-card-text>
        {{ gameData.gameData.notes }}
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title class="d-flex justify-center align-center">
        <h2>Rounds</h2>
      </v-card-title>
      <v-card-text>
        <div v-for="(round, index) in gameData.gameData.rounds" :key="index" class="mb-4">
          <h3>Round {{ round.roundId }}</h3>
          <v-row class="my-2">
            <v-col cols="12">
              <v-icon>mdi-timer</v-icon>
              <span class="ml-2">{{ formatDate(round.roundStart).split(" ")[1] }} - {{ formatDate(round.roundEnd).split(" ")[1] }}</span>
              <span> ({{ formatDuration(round.roundDuration) }})</span>
            </v-col>
          </v-row>
         
          <div class="pl-4 mb-2 text-h5">
          {{ round.roundTotalMakes }} / {{ round.roundTotalAttempts }}
          </div>
          <v-progress-linear
            :model-value="calcMakePercentage(round.roundTotalMakes, round.roundTotalAttempts)"
            height="25"
            :color="getPercentageColor(totalMakePercentage)"
            rounded
          >
            <template v-slot:default="{ value }">
            <strong>{{ Math.round(value) }}%</strong>
            </template>
          </v-progress-linear>

          <v-table class="mt-4">
            <thead>
              <tr>
                <th class="text-center">Distance</th>
                <th class="text-center">Makes / Attempts</th>
                <th class="text-center">Make %</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(station, sIndex) in round.stations" :key="sIndex">
                <td class="text-center">{{ station.distance }}</td>
                <td class="text-center">{{ station.makes }} / {{ station.attempts }}</td>
                <td class="text-center"><v-progress-circular
                :model-value="calcMakePercentage(station.makes, station.attempts)"
                :rotate="-90"
                :size="100"
                :width="15"
                :color="getPercentageColor(calcMakePercentage(station.makes, station.attempts))"
                >
                {{ calcMakePercentage(station.makes, station.attempts) }} %
              </v-progress-circular></td>
              </tr>
            </tbody>
          </v-table>
        </div>
      </v-card-text>
    </v-card>

    <v-btn to="/" class="mt-4">Return to Home</v-btn>
  </v-container>
  <div v-else>
    <p>Game not found.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const gameId = route.params.id;
const gameData = ref(null);
const totalMakePercentage = ref(0);

onMounted(() => {
  const storedGameData = localStorage.getItem(`game-${gameId}`);
  if (storedGameData) {
    gameData.value = JSON.parse(storedGameData);
    totalMakePercentage.value = calcMakePercentage(gameData.value.gameData.gameTotalMakes, gameData.value.gameData.gameTotalAttempts);
  }
});

const calcMakePercentage = (makes, attempts) => {
  if (attempts === 0) {
    return '0%';
  }
  return ((makes / attempts) * 100);
}

const getPercentageColor = (percentage) => {
  if (percentage >= 75) {
    return 'green';
  } else if (percentage >= 50) {
    return 'orange';
  } else {
    return 'red';
  }
};


const formatDuration = (seconds) => {
  if (seconds < 60) {
    return `${Math.floor(seconds)} seconds`;
  } else if (seconds < 3600) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes} minutes ${remainingSeconds} seconds`;
  } else {
    const hours = Math.floor(seconds / 3600);
    const remainingMinutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
    return `${hours} hours ${remainingMinutes} minutes ${remainingSeconds} seconds`;
  }
};
const formatDate = (isoString) => {
  if (!isoString) return '';
  const date = new Date(isoString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  const seconds = String(date.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
};
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}
</style>