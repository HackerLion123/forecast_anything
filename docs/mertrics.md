
# Forecasting Metrics Guide

Understanding when to use each metric is crucial for effective demand and sales forecasting. Each metric has specific strengths and weaknesses depending on your business context.

---

## MAPE (Mean Absolute Percentage Error)

**Formula**: `MAPE = (1/n) * Σ |actual - forecast| / |actual| * 100%`

### Good For:
- Comparing forecast accuracy across products with different scales (e.g., high-volume vs. low-volume items)
- Business stakeholders who prefer percentage-based metrics for easy interpretation
- When relative errors are more important than absolute errors
- Portfolio-level comparisons where items have vastly different demand levels

### Bad/Problematic When:
- **Dealing with zero or near-zero actuals** - MAPE becomes undefined or explodes, making it unusable for intermittent demand or new product forecasting
- **Asymmetric penalty** - Penalizes over-forecasts more heavily than under-forecasts (e.g., 50% over-forecast has larger error than 50% under-forecast)
- **Low-volume items dominate** - Small absolute errors on low-volume items create disproportionately large percentage errors
- **Intermittent demand patterns** - Many zeros in historical data make MAPE unreliable
- **Comparing different products** - Scale-independence can hide the business impact of errors

**Demand Forecasting Context**: Avoid MAPE for slow-moving items, new products, or promotional periods where zeros are common. Better suited for stable, high-volume products.

---

## WAPE (Weighted Absolute Percentage Error)

**Formula**: `WAPE = Σ |actual - forecast| / Σ |actual| * 100%`

Also known as **MAD/Mean Ratio**.

### Good For:
- **Aggregated portfolio accuracy** - Provides overall forecast accuracy across multiple SKUs
- **Handling intermittent demand** - More robust to zeros than MAPE since aggregation in denominator prevents division issues
- **Business-level KPIs** - Useful for reporting overall forecast performance to management
- **Inventory optimization** - Directly relates to total inventory impact across product portfolio
- **When errors need to be weighted by volume** - High-volume items naturally have more influence

### Bad/Problematic When:
- **Need item-level insights** - Masks performance of individual products; good performance on high-volume items can hide poor performance on low-volume ones
- **All actuals are zero** - Still undefined when total actual demand is zero
- **Requires granular feedback** - Doesn't help identify which specific products are problematic
- **Comparing time periods with different volumes** - Can be misleading when comparing seasonal peaks vs. troughs

**Demand Forecasting Context**: Excellent for executive dashboards and overall supply chain performance monitoring. Use alongside item-level metrics for complete visibility.

---

## Bias

**Formula**: `Bias = Σ (forecast - actual) / Σ actual` or `Mean Error = (1/n) * Σ (forecast - actual)`

### Good For:
- **Detecting systematic over/under-forecasting** - Identifies consistent directional errors
- **Inventory cost analysis** - Positive bias (over-forecasting) vs. negative bias (under-forecasting) have different cost implications
- **Model calibration** - Helps identify if your model is systematically optimistic or pessimistic
- **Promotional planning** - Understanding if promotions are consistently over or under-estimated
- **Safety stock decisions** - Directional bias impacts safety stock requirements differently

### Bad/Problematic When:
- **Used alone** - Bias can be zero even with large errors if over/under-forecasts cancel out
- **Short time horizons** - Random fluctuations can mask systematic bias
- **Evaluating absolute accuracy** - Doesn't capture error magnitude, only direction
- **Comparing different products** - Bias percentage varies with scale

**Demand Forecasting Context**: Critical for understanding if you're consistently overstocking (high holding costs) or understocking (lost sales). Always use with other accuracy metrics. Particularly important for:
- Working capital management
- Production planning capacity
- Vendor relationship management (consistent over-orders damage credibility)

---

## RMSE (Root Mean Squared Error)

**Formula**: `RMSE = √[(1/n) * Σ (actual - forecast)²]`

### Good For:
- **Penalizing large errors** - Squares errors, so large deviations are weighted more heavily
- **Statistical model optimization** - Many ML models optimize for MSE/RMSE
- **Demand planning with high service levels** - Large stockouts are more costly, RMSE reflects this
- **Gaussian error assumptions** - When forecast errors are normally distributed
- **Outlier sensitivity** - When you want the metric to be sensitive to occasional large misses

### Bad/Problematic When:
- **Different scales** - Not comparable across products with different demand levels (use RMSE/Mean for scale-free comparison)
- **Outliers are legitimate** - In promotional demand or seasonal spikes, RMSE may overreact
- **Business interpretation** - Harder for non-technical stakeholders to understand than MAE or MAPE
- **Intermittent demand** - Large errors on sporadic demand can dominate the metric
- **Comparing models on different datasets** - Scale-dependent nature makes comparison difficult

**Demand Forecasting Context**: Best used for:
- Continuous review inventory systems where large errors significantly increase costs
- High-value items where stockouts are expensive
- Production planning where capacity constraints make large forecast errors problematic
- Statistical forecasting model development and tuning

Consider using **RMSE/Mean** (CV-RMSE) for comparing across different product scales.

---

## RMSLE (Root Mean Squared Logarithmic Error)

**Formula**: `RMSLE = √[(1/n) * Σ (log(actual + 1) - log(forecast + 1))²]`

### Good For:
- **Heavy right-skewed distributions** - Common in e-commerce and retail (many low sellers, few bestsellers)
- **When under-forecasting is more acceptable than over-forecasting** - Penalizes over-predictions more
- **Wide range of demand magnitudes** - Logarithmic transformation reduces impact of scale
- **Relative differences matter** - Focuses on percentage differences rather than absolute
- **New product forecasting** - When demand could range from very low to very high

### Bad/Problematic When:
- **Over-forecasting is costly** - RMSLE is more lenient on under-forecasts, problematic if stockouts are expensive
- **Need symmetric error treatment** - Biases toward under-forecasting which may not align with business objectives
- **Interpretation for business users** - Logarithmic scale is not intuitive for most stakeholders
- **Near-zero values are critical** - Log transformation can still struggle with very small values
- **Linear cost structures** - When forecast errors have linear cost implications, not exponential

**Demand Forecasting Context**: Useful for:
- E-commerce platforms with long-tail inventory (many low-demand SKUs)
- Marketplace forecasting where demand varies by orders of magnitude
- Situations where overstock costs (warehousing, obsolescence) dominate understock costs
- Marketing campaign impact prediction where effects can vary widely

**Warning**: The asymmetric penalty means RMSLE-optimized models tend to under-forecast, which can lead to frequent stockouts if not properly calibrated.

---

## Choosing the Right Metric

### For Different Forecasting Scenarios:

**Intermittent/Slow-Moving Items**:
- ✅ WAPE, Bias, RMSE (count-based)
- ❌ MAPE

**Fast-Moving/High-Volume Items**:
- ✅ MAPE, WAPE, RMSE, Bias (all work well)
- ⚠️ RMSLE (may under-penalize large errors)

**New Product Launches**:
- ✅ WAPE, RMSLE, Bias
- ❌ MAPE (likely zeros in history)

**Portfolio Management**:
- ✅ WAPE (primary), Bias (secondary)
- ⚠️ MAPE (can be misleading)

**High Service Level Requirements**:
- ✅ RMSE, Bias (under-forecast tracking)
- ⚠️ RMSLE (may under-forecast)

**Cost Minimization Focus**:
- ✅ Weighted metrics based on actual costs (custom)
- ✅ RMSE if large errors disproportionately costly
- ✅ Bias to understand inventory carrying vs. stockout trade-offs

### Best Practice:
**Never rely on a single metric.** Use a combination:
1. **WAPE or RMSE** for overall accuracy
2. **Bias** for directional accuracy
3. **Item-level MAPE or RMSE** for identifying problematic products (where applicable)
4. **Custom business metrics** aligned with actual costs (e.g., lost sales cost, holding cost)