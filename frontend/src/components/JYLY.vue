<template>
    <v-container fill-height d-flex flex-column>
    <h1>JYLY</h1>
      <v-card id="scorecard">
        <v-card-text class="text-center">
          <!-- Add toggle for feet/meters -->
          <div id="score-distance">{{ currentDistance }}</div>
          <v-card-subtitle>{{ measurement }}</v-card-subtitle>
          <div id="score-score">{{ totalScore }}</div>
          <div id="score-station">{{ stationCount }} / 20</div>
          <v-card-subtitle>Rounds</v-card-subtitle>
        </v-card-text>
      </v-card>
      <!-- Testing 
      <div id="stats-table">
        <v-table class="mt-4">
          <!-- Temp data, testing table, use progress bar instead
          <thead>
            <tr>
              <th class="text-center">Distance</th>
              <th class="text-center">Putting</th>
              <th class="text-center">Percentage</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in tableData" :key="item.distance">
              <td class="text-center">{{ item.distance }}</td>
              <td class="text-center">{{ item.putting }}</td>
              <td class="text-center">{{ item.percentage }}</td>
            </tr>
          </tbody>
        </v-table>
      </div>
      <div id="stats-progress">
        <div v-for="item in tableData" :key="item.distance" class="mt-4">
      <div class="d-flex align-center">
        <div style="width: 80px;">{{ item.distance }}</div>
        <v-progress-linear
          :value="item.percentage"
          height="25"
          class="ml-4 mr-2"
          style="flex-grow: 1;"
        >
          <template v-slot:default="{ value }">
            <strong>{{ Math.ceil(value) }}%</strong>
          </template>
        </v-progress-linear>
        <div style="width: 50px; text-align: right;">{{ item.putting }}</div>
      </div>
    </div>
      </div>
    -->
      <v-container class="position-absolute bottom-0 left-0 right-0 w-100">
        <v-row>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(0)">0</v-btn>
          </v-col>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(1)">1</v-btn>
          </v-col>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(2)">2</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(3)">3</v-btn>
          </v-col>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(4)">4</v-btn>
          </v-col>
          <v-col cols="4">
            <v-btn block color="secondary" @click="recordMakes(5)">5</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" class="pb-5">
            <v-btn block color="error" @click="clearScore">Clear Score</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const measurement = ref('Meters');
  const currentDistance = ref(10);
  const makes = ref(0);
  const totalScore = ref(0);
  const stationCount = ref(0);
  
  const recordMakes = (makesCount) => {
    if (stationCount.value >= 20) {
        console.log('Game Over');
        return;
    }

    if (makesCount !== 0) {
        makes.value = makesCount;
        totalScore.value += makes.value * currentDistance.value;
        currentDistance.value = makes.value + 5;
        stationCount.value++;
    }
    else {
        currentDistance.value = 5;
        stationCount.value++;
    }
  };
  
  const clearScore = () => {
    currentDistance.value = 10;
    makes.value = 0;
    totalScore.value = 0;
    stationCount.value = 0;
  };

  const tableData = ref([{
    distance: 10,
    putting: 0,
    percentage: 0
  }, {
    distance: 15,
    putting: 0,
    percentage: 0 
  }, {
    distance: 20,
    putting: 0,
    percentage: 0
  }
  ]);
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