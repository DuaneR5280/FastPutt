<template>
    <v-container>
        <h1>Games</h1>
        <v-row>
            <v-col cols="12" lg="4">

                <v-card>
                    <v-card-title>JYLY</v-card-title>
                    <v-card-text>
                        <p><a href="https://www.dgcoursereview.com/threads/finnish-putting-game.120947/"
                                target="_blank">The original Finnish JYLY game!</a></p>

                    </v-card-text>
                    <v-row>
                        <v-col cols="6">
                            <v-card-actions>
                                <v-btn color="primary" text="How to Play" block variant="text"
                                    @click="reveal = !reveal"></v-btn>
                            </v-card-actions>

                        </v-col>
                        <v-col cols="6">
                            <v-card-actions>
                                <v-btn color="primary" block to="/jyly" text="Play JYLY"></v-btn>
                            </v-card-actions>
                        </v-col>
                    </v-row>

                    <v-expand-transition>
                        <v-sheet v-if="reveal" class="mt-4">

                            <v-card-text>
                                <h2>How to Play</h2>
                                <v-list>
                                    <v-list-item>
                                        <v-list-item-title>5 putters</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Setup markers at 5m, 6m , 7m, 8m, 9m, and
                                            10m</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Start at 10m and record your score (# makes *
                                            distance)</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Move to next distance based on number of
                                            makes</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Repeat 20 times (100 putts)</v-list-item-title>
                                    </v-list-item>
                                </v-list>

                                <v-table>
                                    <thead>
                                        <tr>
                                            <th class="text-left">Number of Makes</th>
                                            <th class="text-left">Distance</th>
                                            <th class="text-left">Points</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="item in tableDataJYLY" :key="item.distance">
                                            <td>{{ item.numMakes }}</td>
                                            <td>{{ item.distance }}</td>
                                            <td v-if="item.points === 0">{{ item.points }}</td>
                                            <td v-else>{{ item.points }} distance</td>
                                        </tr>
                                    </tbody>
                                </v-table>
                            </v-card-text>
                        </v-sheet>
                    </v-expand-transition>

                </v-card>

            </v-col>
            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>1025</v-card-title>
                    <v-card-text>
                        36 putts per round with bonuses for the first and last and all putts made. A total of 1025
                        points is a
                        perfect score.
                    </v-card-text>
                    <v-row>
                        <v-col cols="6">
                            <v-card-actions>
                                <v-btn color="primary" text="How to Play" block variant="text"
                                    @click="revealTtf = !revealTtf"></v-btn>
                            </v-card-actions>

                        </v-col>
                        <v-col cols="6">
                            <v-card-actions>
                                <v-btn color="primary" block to="/1025" text="Play 1025"></v-btn>
                            </v-card-actions>
                        </v-col>
                    </v-row>
                    <v-expand-transition>
                        <v-sheet v-if="revealTtf" class="mt-4">
                            <v-card-text>
                                <h2>How to Play</h2>
                                <v-list>
                                    <v-list-item>
                                        <v-list-item-title>6 putters</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Setup markers at 10', 15', 20', 25', 30', and
                                            35'</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Start at 10' and input # of makes</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Input First & Last makes</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Next >> distance</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Repeat 6 times (36 putts)</v-list-item-title>
                                    </v-list-item>
                                </v-list>
                                <v-alert
                                    text="Input the number of makes and then press the buttons (first/last) to record the bonuses. Use the All button to quickly record all makes and add all the bonuses automatically"
                                    title="Important" type="warning">
                                </v-alert>

                                <v-table>
                                    <thead>
                                        <tr>
                                            <th class="text-left">Distance</th>
                                            <th class="text-left">Points per make</th>
                                            <th class="text-left">Bonus First & Last **</th>
                                            <th class="text-left">All Made Bonus</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="item in tableData1025" :key="item.distance">
                                            <td>{{ item.distance }}</td>
                                            <td>{{ item.points }}</td>
                                            <td>{{ item.bonusFirstLast }}</td>
                                            <td>{{ item.allMadeBonus }}</td>
                                        </tr>
                                    </tbody>
                                </v-table>
                                <v-alert class="my-4"
                                    text="Bonus points a for each, so if you make first & last you'll get the bonus listed x2"
                                    title="** Bonus Points" type="info">

                                </v-alert>
                                <p><strong>Suggestion</strong>: In order to account for variances in wind, lighting, and
                                    ground slope, no more than 2 putts may be thrown from a single location. It is
                                    suggested that you set up a triangle for each tier and throw 2 putts from each
                                    location.</p>


                            </v-card-text>
                        </v-sheet>
                    </v-expand-transition>

                </v-card>
            </v-col>

            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>Circle 1 (C1)</v-card-title>
                    <v-card-text>
                        50 putts per round from progressive distances starting at 15 feet. No points, just stats.

                        <v-row>
                            <v-col cols="6">
                                <v-card-actions>
                                    <v-btn color="primary" text="How to Play" block variant="text"
                                        @click="revealC1 = !revealC1"></v-btn>
                                </v-card-actions>

                            </v-col>
                            <v-col cols="6">
                                <v-card-actions>
                                    <v-btn color="primary" block to="/c1" text="Play c1"></v-btn>
                                </v-card-actions>
                            </v-col>
                        </v-row>
                    </v-card-text>
                    <v-expand-transition>
                        <v-sheet v-if="revealC1" class="mt-4">
                            <v-card-text>
                                <h2>How to Play</h2>
                                <v-list>
                                    <v-list-item>
                                        <v-list-item-title>10 putters</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Setup markers at 15', 20', 25', 30', and
                                            35'</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Start at 15' and record your # of makes</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Move to next distance</v-list-item-title>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-title>Repeat 5 times (50 putts)</v-list-item-title>
                                    </v-list-item>
                                </v-list>
                                <p>Quickly knock out a large volume of putts (250, 500, 750, 1000) for daily practice.
                                    The distances and number of putts from each station allow for easy stat calculations
                                    to monitor improvement.</p>
                                <br>
                                <p>35' is outside of the circle and is intentional to practice C1 edge putts.</p>

                            </v-card-text>
                        </v-sheet>
                    </v-expand-transition>
                </v-card>
            </v-col>
            <!-- C2
            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>Circle 2 (C2)</v-card-title>
                    <v-card-text>
                        50 putts per round from progressive distances starting at 40 feet. No points, just stats.
                        <v-divider class="my-4" color="#6ef137"></v-divider>
                        <h2>How to Play</h2>
                        <v-list>
                            <v-list-item>
                                <v-list-item-title>10 putters</v-list-item-title>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-title>Setup markers at 40', 45', 50', 55', and 60'</v-list-item-title>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-title>Start at 15' and record your # of makes</v-list-item-title>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-title>Move to next distance</v-list-item-title>
                            </v-list-item>
                            <v-list-item>
                                <v-list-item-title>Repeat 5 times (50 putts)</v-list-item-title>
                            </v-list-item>
                        </v-list>
                        <p>Quickly knock out a large volume of putts (250, 500, 750, 1000) for daily practice. The
                            distances and number of putts from each station allow for easy stat calculations to monitor
                            improvement.</p>
                        <v-btn class="mt-4" color="primary" to="/c2">Play C2</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
        -->
            <!-- PP360 
            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>PP360</v-card-title>
                    <v-card-text>
                        Throw 50 putts from varying distances. Complete two rounds for 100 total putts and strive for
                        that perfect 360.
                        <!-- game scorecard

                        | Distance | Points | First In | Last In | All Made |
                        | :------: |:-----: | :------: | :-----: | :-----:  |
                        | 10'      | 1      | 2        | 2       | 5        |
                        | 15'      | 1      | 2        | 3       | 10       |
                        | 20'      | 1      | 3        | 4       | 15       |
                        | 25'      | 1      | 5        | 6       | 20       |
                        | 30'      | 1      | 8        | 10      | 25       |

                        <br>
                        <v-btn class="mt-4" color="disabled" to="/pp360">Play PP360</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>Ladder</v-card-title>
                    <v-card-text>
                        Ladder description
                        <br>
                        <v-btn class="mt-4" color="disabled" to="/ladder">Play Ladder</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>Free Putt</v-card-title>
                    <v-card-text>
                        No nonsense practice. Select the number of putters, pick a distance, putt, enter made putts,
                        repeat or not.
                        <v-btn class="mt-4" color="disabled" to="/ladder">Play Free Putt</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>50</v-card-title>
                    <v-card-text>
                        Focus and work on those trouble distances. Throw 50 putts from a specific distance.
                        <br>
                        <v-btn class="mt-4" color="disabled" to="/50">Play 50</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" lg="4">
                <v-card>
                    <v-card-title>Challenges</v-card-title>
                    <v-card-text>
                        Take a break from the monotony and complete a challenge!
                        <br>
                        <v-btn class="mt-4" color="disabled" to="/challenges">Play a Challenge</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12">
                <v-card>
                    <v-card-title>Custom</v-card-title>
                    <v-card-text>
                        Create a custom game, routine, or challenge.
                        <br>
                        <v-btn class="mt-4" color="disabled" to="/create-custom">Create Custom</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
        -->
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';
// import JYLY from '../components/JYLY.vue';
// import TenTwentyFive from '../components/TenTwentyFive.vue';

const reveal = ref(false);
const revealTtf = ref(false);
const revealC1 = ref(false);

const tableDataJYLY = ref([
    { numMakes: 0, distance: "5m / 16.4 ft", points: 0 },
    { numMakes: 1, distance: "6m / 19.7 ft", points: "1 *" },
    { numMakes: 2, distance: "7m / 22.9 ft", points: "2 *" },
    { numMakes: 3, distance: "8m / 26.2 ft", points: "3 *" },
    { numMakes: 4, distance: "9m / 29.5 ft", points: "4 *" },
    { numMakes: 5, distance: "10m / 32.8 ft", points: "5 *" },
]);

const tableData1025 = ref([
    { distance: "10'", points: 10, bonusFirstLast: "+5", allMadeBonus: 10 },
    { distance: "15'", points: 15, bonusFirstLast: "+5", allMadeBonus: 15 },
    { distance: "20'", points: 20, bonusFirstLast: "+5", allMadeBonus: 20 },
    { distance: "25'", points: 25, bonusFirstLast: "+5", allMadeBonus: 25 },
    { distance: "30'", points: 30, bonusFirstLast: "+10", allMadeBonus: 30 },
    { distance: "35'", points: 35, bonusFirstLast: "+10", allMadeBonus: 35 },
]);

</script>