<template>
  <v-container v-if="gameData">
    <h1>Game Summary</h1>
    <v-subheader class="text-caption text-grey-lighten-1 mb-2">{{ gameId }}</v-subheader>

    <v-card class="mb-4">
      <v-card-title>Game Session</v-card-title>
      <div class="mx-4 text-subtitle-2 text-grey-lighten-1">{{ formatDate(gameData.gameStart).split(" ")[0] }}</div>
      <v-card-text>
        <v-row dense>
          <v-col cols="12" sm="4" class="text-center">
            <v-icon>mdi-clock-start</v-icon>
            <div class="text-subtitle-1">Start</div>
            <div class="text-h6">{{ formatDate(gameData.gameStart).split(" ")[1] }}</div>
          </v-col>
          <v-col cols="12" sm="4" class="text-center">
            <v-icon>mdi-timer</v-icon>
            <div class="text-subtitle-1">Duration</div>
            <div class="text-h6">{{ formatDuration(gameData.gameDuration) }}</div>
          </v-col>
          <v-col cols="12" sm="4" class="text-center">
            <v-icon>mdi-clock-end</v-icon>
            <div class="text-subtitle-1">End</div>
            <div class="text-h6">{{ formatDate(gameData.gameEnd).split(" ")[1] }}</div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card prepend-icon="mdi-target" title="Total Putts" class="mb-4">
      <v-card-text class="text-center">
        <div class="text-h3 mb-2">
          {{ gameData.totalMakes }} / {{ gameData.totalAttempts }}
        </div>
        <v-progress-linear
          :model-value="totalMakePercentage"
          height="30"
          :color="getPercentageColor(totalMakePercentage)"
          rounded
          class="text-h6"
        >
          <template v-slot:default="{ value }">
            <strong>{{ Math.round(value) }}%</strong>
          </template>
        </v-progress-linear>
      </v-card-text>
    </v-card>

    <v-card class="mb-4" title="Performance Goals">
      <v-card-text>
        <v-row dense>
          <v-col cols="6" sm="6" class="text-center">
            <v-progress-circular
              :model-value="totalMakePercentage"
              :rotate="-90"
              :size="100"
              :width="15"
              :color="getPercentageColor(totalMakePercentage)"
            >
              {{ Math.round(totalMakePercentage) }} %
            </v-progress-circular>
            <div class="text-subtitle-1 mt-2">C1 Goal (Session)</div>
          </v-col>
          <v-col cols="6" sm="6" class="text-center">
            <v-progress-circular
              :model-value="20"
              :rotate="-90"
              :size="100"
              :width="15"
              :color="getPercentageColor(20)"
            >
              20 %
            </v-progress-circular>
            <div class="text-subtitle-1 mt-2">Daily Goal (500 putts)</div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card class="mb-4" v-if="gameData.conditions">
      <v-card-title>Conditions</v-card-title>
      <v-card-text>{{ gameData.conditions }}</v-card-text>
    </v-card>

    <v-card class="mb-4" v-if="gameData.notes">
      <v-card-title>Notes</v-card-title>
      <v-card-text>{{ gameData.notes }}</v-card-text>
    </v-card>

    <v-card class="mb-4">
      <v-card-title class="text-center">Rounds</v-card-title>
      <v-card-text>
        <v-card
          v-for="(round, index) in gameData.rounds"
          :key="index"
          class="mb-6 pa-4"
          variant="outlined"
        >
          <h3 class="text-h6 mb-2">Round {{ round.roundId }}</h3>
          <div class="d-flex align-center mb-2">
            <v-icon small class="mr-1">mdi-clock</v-icon>
            <span class="text-body-2"
              >{{ formatDate(round.roundStart).split(" ")[1] }} -
              {{ formatDate(round.roundEnd).split(" ")[1] }}</span
            >
            <span class="text-caption ml-1"
              >({{ formatDuration(round.roundDuration) }})</span
            >
          </div>

          <div class="mb-2 text-h5 text-center">
            {{ round.roundTotalMakes }} / {{ round.roundTotalAttempts }}
          </div>
          <v-progress-linear
            :model-value="calcMakePercentage(round.roundTotalMakes, round.roundTotalAttempts)"
            height="25"
            :color="getPercentageColor(calcMakePercentage(round.roundTotalMakes, round.roundTotalAttempts))"
            rounded
            class="mb-4"
          >
            <template v-slot:default="{ value }">
              <strong>{{ Math.round(value) }}%</strong>
            </template>
          </v-progress-linear>

          <v-expansion-panels>
            <v-expansion-panel title="View Station Details">
              <v-expansion-panel-text>
                <div v-if="$vuetify.display.smAndDown">
                  <v-card
                    v-for="(station, sIndex) in round.stations"
                    :key="sIndex"
                    class="mb-3 pa-2 d-flex flex-column align-center"
                    variant="flat"
                  >
                    <div class="font-weight-bold mb-1">Distance: {{ station.distance }}</div>
                    <v-progress-circular
                      :model-value="calcMakePercentage(station.makes, station.attempts)"
                      :rotate="-90"
                      :size="80"
                      :width="10"
                      :color="getPercentageColor(calcMakePercentage(station.makes, station.attempts))"
                      class="mb-1"
                    >
                      <span class="text-body-2">{{ Math.round(calcMakePercentage(station.makes, station.attempts)) }}%</span>
                    </v-progress-circular>
                    <div class="text-caption">
                      ({{ station.makes }} / {{ station.attempts }})
                    </div>
                  </v-card>
                </div>
                <v-table v-else class="mt-4">
                  <thead>
                    <tr>
                      <th class="text-center">Distance</th>
                      <th class="text-center">Make %</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(station, sIndex) in round.stations" :key="sIndex">
                      <td class="text-center">{{ station.distance }}</td>
                      <td class="text-center">
                        <v-progress-circular
                          :model-value="calcMakePercentage(station.makes, station.attempts)"
                          :rotate="-90"
                          :size="80"
                          :width="10"
                          :color="getPercentageColor(calcMakePercentage(station.makes, station.attempts))"
                        >
                          {{ Math.round(calcMakePercentage(station.makes, station.attempts)) }} %
                        </v-progress-circular>
                        <div class="text-caption mt-1">({{ station.makes }} / {{ station.attempts }})</div>
                      </td>
                    </tr>
                  </tbody>
                </v-table>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-card>
      </v-card-text>
    </v-card>

    <v-btn to="/" class="mt-4" block>Return to Home</v-btn>
  </v-container>
  <div v-else>
    <p>Game not found.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useDisplay } from 'vuetify'; // Import useDisplay

const route = useRoute();
const gameId = route.params.id;
const gameData = ref(null);
const totalMakePercentage = ref(0);
const display = useDisplay(); // Use the display composable

onMounted(async () => {
  try {
    const response = await fetch(`/api/games/${gameId}`);
    if (!response.ok) {
      throw new Error('Failed to fetch game data');
    }
    const data = await response.json();
    gameData.value = data;
    totalMakePercentage.value = calcMakePercentage(data.totalMakes, data.totalAttempts);
  } catch (err) {
    console.error('Error loading game:', err);
    gameData.value = null;
    totalMakePercentage.value = 0;
  }
});

const calcMakePercentage = (makes, attempts) => {
  if (attempts === 0) {
    return 0; // Return a number, not a string, for model-value
  }
  return parseFloat(((makes / attempts) * 100).toFixed(1)); // Return a number, rounded
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
    return `${minutes}m ${remainingSeconds}s`; // Shorter format for duration
  } else {
    const hours = Math.floor(seconds / 3600);
    const remainingMinutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = Math.floor(seconds % 60); // Ensure seconds are floored
    return `${hours}h ${remainingMinutes}m ${remainingSeconds}s`;
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
/* No specific scoped styles needed if using Vuetify's utility classes effectively */
/* benjamin felipe rodarte */
</style>

