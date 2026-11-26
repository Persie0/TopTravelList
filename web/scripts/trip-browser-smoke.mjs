// Run against a built Vite preview with Playwright installed separately.
import {chromium} from 'playwright';
import assert from 'node:assert/strict';
const browser=await chromium.launch({headless:true});
try{
 const page=await browser.newPage({viewport:{width:1440,height:950}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('dialog',d=>d.accept());
 await page.goto('http://127.0.0.1:4173/');await page.locator('#routesTab').waitFor();await page.locator('#routesTab').click();
 await page.locator('#routeCountry').selectOption('AT');await page.locator('.route-advanced summary').click();await page.locator('#routeMin').selectOption('0');
 await page.locator('#routeGenerate').click();await page.locator('#routeUse').click();await page.locator('.route-stop').first().waitFor();
 const count=await page.locator('.route-stop').count();assert.ok(count>1);
 await page.locator('#routeJump').click();await page.locator('#tripName').fill('Austria adventure');await page.locator('#tripName').press('Tab');
 await page.locator('#tripDays').fill('3');await page.locator('#tripDays').press('Tab');
 assert.equal(await page.locator('.trip-day').count(),3);
 await page.locator('[data-trip-tab="progress"]').click();await page.locator('.trip-stop-detail summary').first().click();
 await page.locator('.trip-stop-detail').first().locator('[data-field="priority"]').check();
 await page.locator('.trip-stop-detail').first().locator('[data-field="visited"]').check();
 await page.locator('[data-trip-tab="stats"]').click();assert.ok(await page.getByText('Must-see catalog coverage').isVisible());
 await page.locator('[data-trip-tab="budget"]').click();await page.locator('[data-budget="daily"]').fill('50');await page.locator('[data-budget="daily"]').press('Tab');assert.ok(await page.getByText('Estimated total').isVisible());
 await page.locator('#tripSave').click();const saved=await page.locator('#tripLibrary').inputValue();assert.ok(saved);
 await page.reload();await page.locator('#routesTab').click();await page.locator('#routeJump').click();assert.equal(await page.locator('#tripName').inputValue(),'Austria adventure');assert.equal(await page.locator('.route-stop').count(),count);assert.equal(await page.locator('#tripLibrary').inputValue(),saved);
 await page.locator('[data-trip-tab="progress"]').click();await page.locator('.trip-stop-detail summary').first().click();assert.ok(await page.locator('.trip-stop-detail').first().locator('[data-field="visited"]').isChecked());await page.locator('#tripNew').click();assert.ok(await page.locator('#tripFind').isVisible());await page.locator('#tripUndo').click();assert.equal(await page.locator('#tripName').inputValue(),'Austria adventure');assert.equal(await page.locator('.route-stop').count(),count);
 await page.locator('.trip-tools summary').click();const download=page.waitForEvent('download');await page.locator('#tripJson').click();assert.match((await download).suggestedFilename(),/\.json$/);
 await page.setViewportSize({width:390,height:844});await page.locator('[data-trip-tab="days"]').click();assert.equal(await page.locator('.trip-day').count(),3);
 assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth+2),'mobile layout must not overflow horizontally');
 await page.locator('#routeDiscover').click();await page.locator('[data-remove]').first().click();assert.equal(await page.locator('.route-stop').count(),count-1);await page.locator('#routeUndo').click();assert.equal(await page.locator('.route-stop').count(),count);await page.locator('#statisticsTab').click();await page.locator('#customChartOutput').waitFor();await page.locator('#places').click();await page.locator('#resultTitle').waitFor();assert.equal(await page.locator('#atlasFilters').isVisible(),false);await page.locator('#filterToggle').click();assert.ok(await page.locator('#atlasFilters').isVisible());
 assert.deepEqual(errors,[]);console.log('Desktop/mobile route studio smoke test passed.');
}finally{await browser.close()}
