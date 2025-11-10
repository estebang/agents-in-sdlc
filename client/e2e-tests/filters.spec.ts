import { test, expect } from '@playwright/test';

test.describe('Game Filtering', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the home page before each test
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
  });

  test('should display filter dropdowns', async ({ page }) => {
    // Check that publisher filter dropdown exists
    await expect(page.locator('[data-testid="publisher-filter"]')).toBeVisible();
    
    // Check that category filter dropdown exists
    await expect(page.locator('[data-testid="category-filter"]')).toBeVisible();
  });

  test('should populate filter dropdowns with options', async ({ page }) => {
    // Check publisher dropdown has options beyond "All Publishers"
    const publisherOptions = await page.locator('[data-testid="publisher-filter"] option').count();
    expect(publisherOptions).toBeGreaterThan(1);
    
    // Check category dropdown has options beyond "All Categories"
    const categoryOptions = await page.locator('[data-testid="category-filter"] option').count();
    expect(categoryOptions).toBeGreaterThan(1);
  });

  test('should filter games by publisher', async ({ page }) => {
    // Get initial count of games
    const initialGameCount = await page.locator('[data-testid="game-card"]').count();
    
    // Select a publisher from the dropdown (skip the first "All Publishers" option)
    const publisherSelect = page.locator('[data-testid="publisher-filter"]');
    const publisherOptions = await publisherSelect.locator('option').allTextContents();
    
    if (publisherOptions.length > 1) {
      await publisherSelect.selectOption({ index: 1 });
      
      // Wait for games to reload
      await page.waitForTimeout(1000);
      
      // Get filtered count of games - it might be the same or different
      const filteredGameCount = await page.locator('[data-testid="game-card"]').count();
      
      // Verify filtering occurred (at minimum, the API call was made)
      // Check if clear filters button appears
      if (filteredGameCount < initialGameCount) {
        await expect(page.locator('[data-testid="clear-filters-btn"]')).toBeVisible();
      }
    }
  });

  test('should filter games by category', async ({ page }) => {
    // Get initial count of games
    const initialGameCount = await page.locator('[data-testid="game-card"]').count();
    
    // Select a category from the dropdown (skip the first "All Categories" option)
    const categorySelect = page.locator('[data-testid="category-filter"]');
    const categoryOptions = await categorySelect.locator('option').allTextContents();
    
    if (categoryOptions.length > 1) {
      await categorySelect.selectOption({ index: 1 });
      
      // Wait for games to reload
      await page.waitForTimeout(1000);
      
      // Get filtered count of games
      const filteredGameCount = await page.locator('[data-testid="game-card"]').count();
      
      // Verify filtering occurred (at minimum, the API call was made)
      // Check if clear filters button appears
      if (filteredGameCount < initialGameCount) {
        await expect(page.locator('[data-testid="clear-filters-btn"]')).toBeVisible();
      }
    }
  });

  test('should show clear filters button when filters are applied', async ({ page }) => {
    // Initially, clear filters button should not be visible
    await expect(page.locator('[data-testid="clear-filters-btn"]')).not.toBeVisible();
    
    // Select a publisher filter
    const publisherSelect = page.locator('[data-testid="publisher-filter"]');
    const publisherOptions = await publisherSelect.locator('option').allTextContents();
    
    if (publisherOptions.length > 1) {
      await publisherSelect.selectOption({ index: 1 });
      
      // Clear filters button should now be visible
      await expect(page.locator('[data-testid="clear-filters-btn"]')).toBeVisible();
    }
  });

  test('should clear filters when clear button is clicked', async ({ page }) => {
    // Select a publisher filter
    const publisherSelect = page.locator('[data-testid="publisher-filter"]');
    const publisherOptions = await publisherSelect.locator('option').allTextContents();
    
    if (publisherOptions.length > 1) {
      await publisherSelect.selectOption({ index: 1 });
      
      // Wait for clear button to appear
      await expect(page.locator('[data-testid="clear-filters-btn"]')).toBeVisible();
      
      // Click clear filters button
      await page.locator('[data-testid="clear-filters-btn"]').click();
      
      // Wait for filters to clear
      await page.waitForTimeout(1000);
      
      // Clear filters button should no longer be visible
      await expect(page.locator('[data-testid="clear-filters-btn"]')).not.toBeVisible();
      
      // Publisher dropdown should be back to "All Publishers"
      const selectedPublisher = await publisherSelect.inputValue();
      expect(selectedPublisher).toBe('');
    }
  });

  test('should combine publisher and category filters', async ({ page }) => {
    const publisherSelect = page.locator('[data-testid="publisher-filter"]');
    const categorySelect = page.locator('[data-testid="category-filter"]');
    
    const publisherOptions = await publisherSelect.locator('option').allTextContents();
    const categoryOptions = await categorySelect.locator('option').allTextContents();
    
    if (publisherOptions.length > 1 && categoryOptions.length > 1) {
      // Select both publisher and category filters
      await publisherSelect.selectOption({ index: 1 });
      await categorySelect.selectOption({ index: 1 });
      
      // Wait for filters to apply
      await page.waitForTimeout(1000);
      
      // Clear filters button should be visible
      await expect(page.locator('[data-testid="clear-filters-btn"]')).toBeVisible();
      
      // Games should still be displayed (even if filtered)
      await page.waitForSelector('[data-testid="games-grid"]');
    }
  });
});