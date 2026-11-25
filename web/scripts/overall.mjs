import Decimal from 'decimal.js';
export function overall(scores, weights) {
  if (!Object.keys(weights).every(k => Number.isFinite(scores[k]))) return null;
  return Object.entries(weights).reduce((sum,[k,w]) => sum.plus(new Decimal(scores[k]).times(w)),new Decimal(0)).times(10).toNumber();
}
