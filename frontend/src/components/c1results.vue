<template>
    <v-container>
      <h2>Game Results</h2>
      <div v-if="rounds.length > 0" v-for="(round, roundIndex) in rounds" :key="roundIndex">
        <h3>Round {{ roundIndex + 1 }}</h3>
        <v-table>
          <thead>
            <tr>
              <th class="text-left">Distance</th>
              <th class="text-left">Makes</th>
              <th class="text-left">Make %</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(station, index) in round" :key="index">
              <td>{{ station.distance }}</td>
              <td>{{ station.makes }}</td>
              <td>{{ calculateStationPercentage(station.makes, station.attempts) }}</td>
            </tr>
          </tbody>
        </v-table>
      </div>
      <div v-if="rounds.length > 0">
        <h3>Session Stats</h3>
        <p>Total Score: {{ sessionTotalScore }}</p>
        <p>Total Attempts: {{ sessionTotalAttempts }}</p>
        <p>Overall Make %: {{ calculateSessionPercentage() }}</p>
        <v-btn class="mt-4" @click="resetGame">Play Again</v-btn>
      </div>
      <div v-else>
        <p>No Game Data Found</p>
        <v-btn class="mt-4" @click="resetGame">Play Game</v-btn>
      </div>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  const route = useRoute();
  const router = useRouter();
  
  const gameId = route.params.gameId;
  const rounds = ref([]);
  const sessionTotalScore = ref(0);
  const sessionTotalAttempts = ref(0);
  
  onMounted(() => {
    console.log('Game ID:', gameId); // Debugging
  
    const storedRounds = localStorage.getItem(`c1-rounds-${gameId}`);
  
    if (storedRounds) {
      rounds.value = JSON.parse(storedRounds);
      console.log('Parsed Rounds:', rounds.value); // Debugging
      updateSessionStats();
    } else {
      console.log('No rounds found in local storage.');
    }
  });
  
  const calculateStationPercentage = (makes, attempts) => {
    if (attempts === 0) {
      return '0%';
    }
    return ((makes / attempts) * 100).toFixed(2) + '%';
  };
  
  const updateSessionStats = () => {
    rounds.value.forEach(round => {
      round.forEach(station => {
        sessionTotalScore.value += station.makes;
        sessionTotalAttempts.value += station.attempts;
      });
    });
  };
  
  const calculateSessionPercentage = () => {
    if (sessionTotalAttempts.value === 0) {
      return '0%';
    }
    return ((sessionTotalScore.value / sessionTotalAttempts.value) * 100).toFixed(2) + '%';
  };
  
  const resetGame = () => {
    router.push('/c1');
  };
  </script>