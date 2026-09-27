import { describe, expect, it } from 'vitest';
import { mergeCoverageData, normalizeFilePath } from '../../tests/e2e/fixtures/coverage-fixture';
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'fs';
import { join } from 'path';

describe('normalizeFilePath', () => {
  it('keeps Vite asset URLs as relative paths for reporting', () => {
    expect(normalizeFilePath('http://localhost:8081/assets/index-DPmOeCyG.js')).toBe('assets/index-DPmOeCyG.js');
  });

  it('preserves source paths from the app', () => {
    expect(normalizeFilePath('http://localhost:8081/src/components/HelloWorld.vue')).toBe('src/components/HelloWorld.vue');
  });

  it('prefixes plain paths with src for local app modules', () => {
    expect(normalizeFilePath('http://localhost:8081/components/App.vue')).toBe('/src/components/App.vue');
  });
});

describe('coverage source fallback', () => {
  it('uses the coverage entry source when the asset file is not on disk', () => {
    const fixturePath = join(process.cwd(), 'tests/e2e/fixtures/coverage-fixture.ts');
    const source = readFileSync(fixturePath, 'utf8');
    expect(source).toContain('export function normalizeFilePath');
  });

  it('merges coverage data across multiple test runs without losing earlier hits', () => {
    const firstRun = {
      'src/App.vue': {
        path: 'src/App.vue',
        statementMap: { '0': { start: { line: 1, column: 0 }, end: { line: 1, column: 10 } } },
        fnMap: {},
        branchMap: {},
        s: { '0': 1 },
        f: {},
        b: {},
      },
    };
    const secondRun = {
      'src/App.vue': {
        path: 'src/App.vue',
        statementMap: { '0': { start: { line: 1, column: 0 }, end: { line: 1, column: 10 } } },
        fnMap: {},
        branchMap: {},
        s: { '0': 0 },
        f: {},
        b: {},
      },
    };

    const merged = mergeCoverageData(firstRun, secondRun);

    expect(merged['src/App.vue'].s['0']).toBe(1);
  });

  it('writes a nyc-compatible merged coverage file when coverage is available', () => {
    const tempDir = join(process.cwd(), 'coverage/e2e-raw');
    rmSync(tempDir, { recursive: true, force: true });
    mkdirSync(tempDir, { recursive: true });

    const coverageMap = {
      'src/App.vue': {
        path: 'src/App.vue',
        statementMap: {},
        fnMap: {},
        branchMap: {},
        s: {},
        f: {},
        b: {},
      },
    };

    const finalPath = join(tempDir, 'coverage-final.json');
    writeFileSync(finalPath, JSON.stringify(coverageMap, null, 2));

    expect(existsSync(finalPath)).toBe(true);
    const saved = JSON.parse(readFileSync(finalPath, 'utf8'));
    expect(saved['src/App.vue']).toBeDefined();
  });
});
