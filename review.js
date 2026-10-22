'use strict';
const pairs = JSON.parse(document.getElementById('review-data').textContent);
const choices = new Map(pairs.map(p => [p.asset_id, p.decision.recommended_version]));
const container = document.getElementById('pairs');
const nodes = new Map();
function element(tag, text, className) {
  const e = document.createElement(tag);
  if (text !== undefined) e.textContent = text;
  if (className) e.className = className;
  return e;
}
function refresh() {
  const count = {A: 0, B: 0, neither: 0};
  for (const p of pairs) {
    const selected = choices.get(p.asset_id);
    count[selected || 'neither']++;
    const row = nodes.get(p.asset_id);
    for (const input of row.querySelectorAll('input[type=radio]')) {
      input.checked = (selected || 'neither') === input.value;
      input.closest('label').classList.toggle('chosen', input.checked);
    }
  }
  document.getElementById('summary').textContent = `已选 A ${count.A} 项 · B ${count.B} 项 · 两版返修 ${count.neither} 项`;
}
for (const p of pairs) {
  const article = element('article'); article.id = p.asset_id;
  article.append(element('h2', p.name), element('p', p.asset_id, 'muted'));
  const rec = p.decision.recommended_version ? `推荐 ${p.decision.recommended_version}` : '推荐：两版都待返修';
  article.append(element('p', `${rec} — ${p.decision.reason}`, 'recommendation'));
  const options = element('div', undefined, 'options');
  for (const version of ['A', 'B']) {
    const item = p.versions[version];
    const label = element('label', undefined, 'option');
    const input = document.createElement('input'); input.type = 'radio'; input.name = p.asset_id; input.value = version;
    input.disabled = !item.master;
    input.addEventListener('change', () => { choices.set(p.asset_id, version); refresh(); });
    label.append(input, element('strong', `选 ${version}`));
    if (item.thumbnail) {
      const img = document.createElement('img'); img.src = item.thumbnail; img.alt = `${p.name} ${version}版缩略图`; img.width = 640; img.height = 360;
      label.append(img);
    } else label.append(element('p', '本版未生成'));
    label.append(element('p', item.status === 'needs_revision' ? '待返修候选' : '已查看的创意候选', 'muted'));
    options.append(label);
  }
  article.append(options);
  const reject = element('label', undefined, 'reject');
  const input = document.createElement('input'); input.type = 'radio'; input.name = p.asset_id; input.value = 'neither';
  input.addEventListener('change', () => { choices.set(p.asset_id, null); refresh(); });
  reject.append(input, document.createTextNode('两版都待返修')); article.append(reject);
  const links = element('p', undefined, 'links');
  for (const version of ['A', 'B']) {
    const item = p.versions[version];
    if (!item.master) continue;
    const a = element('a', `${version}版独立原图`); a.href = item.master; a.target = '_blank'; a.rel = 'noopener'; links.append(a);
  }
  const detail = element('details'); detail.append(element('summary', '查看原始要求与视觉备注'));
  detail.append(element('p', p.source_prompt));
  for (const version of ['A', 'B']) detail.append(element('p', `${version}：${p.versions[version].visual_notes.join('；')}`));
  article.append(links, detail); container.append(article); nodes.set(p.asset_id, article);
}
function buildExport() {
  return {
    schema: 'directorx-user-ab-selection/1',
    exported_at_utc: new Date().toISOString(),
    scope: 'P0 only; creative candidates, no canvas changes',
    items: pairs.map(p => {
      const version = choices.get(p.asset_id);
      const item = version ? p.versions[version] : null;
      return {asset_id: p.asset_id, target: p.target, name: p.name, selected_version: version,
        status: version ? 'user_selected_candidate' : 'both_need_revision',
        master: item?.master || null, thumbnail: item?.thumbnail || null, sha256: item?.sha256 || null,
        generated_by: item?.generated_by || null, preview_kind: p.preview_kind,
        assistant_recommended_version: p.decision.recommended_version};
    })
  };
}
window.buildExport = buildExport;
document.getElementById('export').addEventListener('click', () => {
  const blob = new Blob([JSON.stringify(buildExport(), null, 2) + '\n'], {type: 'application/json;charset=utf-8'});
  const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'directorx-my-ab-selection.json';
  document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  document.getElementById('notice').textContent = '已导出你的选择。素材和原推荐没有被改写。';
});
document.getElementById('reset').addEventListener('click', () => {
  for (const p of pairs) choices.set(p.asset_id, p.decision.recommended_version);
  refresh(); document.getElementById('notice').textContent = '已恢复助手推荐。关闭本页前请导出需要保留的选择。';
});
refresh();
