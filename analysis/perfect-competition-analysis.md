# Perfect Competition — Analysis

## 1. Why tomatoes stop at ~10 beds

Tomatoes make $8,800 per bed, which is much more than carrots, but the model still plants only 10 tomato beds even though 20 were allowed. They didn't stop because they ran out of space — they stopped because the economics stopped working. At 10 beds, tomato marginal cost is $8,248.59 and the price is $8,800, so that bed still earns $551.41. But at bed 11, marginal cost jumps to $9,390.72, which is higher than the price. That means any tomato bed past 10 would lose money. Once marginal cost rises above price, the fact that tomatoes are the "money crop" doesn't matter anymore. The model stops at 10 because that's where P = MC switches from profitable to unprofitable, even though 10 more tomato beds were still available.

![Tomato marginal cost by bed](figures/tomato-beds-fig1.png)

## 2. Which constraints bind — and what relaxing one is worth

Carrots and mesclun stop because they hit their bed limits while they're still making money, which means the cap — not the economics — is what stops them. For carrots, the farm uses all 20 beds. At bed 20, carrot marginal cost is $1,688.95 and the price is $2,094, so the farm is still earning $405.05 on that bed. If the farm could plant a 21st bed, it would cost $1,741.51 and still earn $352.49. That $352.49 is the shadow price — what one more carrot bed would be worth. Mesclun is the same story. The farm uses all 30 mesclun beds. At bed 30, marginal cost is $2,420.10 and the price is $2,700, leaving $279.90 of room. A 31st bed would cost $2,453.53 and earn $246.47, so $246.47 is mesclun's shadow price. The other limits don't matter: the plan uses only 60 of the 64 total beds and about 3.16 of the 4 temp workers, so those constraints aren't stopping anything. The simple takeaway is that carrot and mesclun land are worth buying first, because each extra bed would add profit, while more total land or more temp labor wouldn't change the plan at all.

## 3. The tomato MC dip at ~6 beds

In the standalone tomato schedule, marginal cost jumps at bed 5 and then drops at bed 6. Bed 5 costs $7,660.86, but bed 6 costs $4,906.28. The dip happens because of a change in who is doing the work, not because tomatoes suddenly get easier to grow. At bed 5, tomatoes are still using almost all of the farmer's expensive hours at $34.72/hr. Only a tiny bit spills over to the cheaper temp labor. By bed 6, the farmer's 720 hours are completely used up, so all of bed 6's labor is priced at the cheaper $17.36/hr temp rate. Even though bed 6 needs more hours than bed 5, the wage drops by half, and that makes the cost fall. After that, every extra hour is at the same temp-labor rate, so nothing else gets cheaper, and diminishing returns push marginal cost back up. The simple lesson is that marginal cost depends on input prices as much as on the number of hours — when the wage changes, the cost curve can dip even while hours per bed keep rising.

![Tomato MC dip](figures/tomato-mc-dip-fig3.png)

## 4. Why grow crops that lose money on their own

Even though carrots and mesclun look unprofitable when grown on their own, the shutdown rule explains why they still belong in the joint plan. What matters is whether the price covers average variable cost, not fixed cost or the marginal cost of the last bed. At the plan's actual endpoints, both crops clear that bar. For carrots at 20 beds, AVC is $1,918.45 against a $2,094 price. For mesclun at 30 beds, AVC is $2,430.74 against a $2,700 price. Carrot AVC stays below price at every bed count from 1 through 20. Mesclun's does not — it briefly rises above price at beds 13 and 14 before falling back below — but what matters is the level actually planted: at 30 beds, mesclun's AVC is back under price. Since P ≥ AVC at the plan's endpoints, both carrots and mesclun should be grown.


## Against the Stage 1 hypothesis

In Stage 1, I predicted 6 tomato, 20 carrot, and 24 mesclun beds. Carrots were the one part I got exactly right — they stay cheap to grow and never come close to their price, so taking the full 20-bed cap was correct. Tomatoes were a directionally right but size-wrong prediction. I expected them to stop early because their diminishing returns are steep, and that part is true, but I underestimated how much room their high $8,800 price gives them. Their MC curve starts low enough that it doesn't cross price until bed 11, so the model planted 10 instead of 6. Mesclun was a different mistake entirely. I stopped at 24 out of caution, but mesclun's marginal cost never gets close to its $2,700 price — even one bed past the cap. Nothing in the economics justified stopping early, so the model went all the way to 30. Carrots were right for the right reason; tomatoes were right in direction but wrong in magnitude; mesclun was a pure judgment miss from not checking where MC meets price.
