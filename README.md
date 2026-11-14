# RideTube with a Close button

[RideTube](https://github.com/JustAnotherPU/RideTube) by JustAnotherPU, with one addition: Close ends the video
and goes back to the list (also proposed upstream: JustAnotherPU/RideTube#6).

- `close-video`: the branch the MGU Store installs from (source `Asksket/ridetube`, branch `close-video`). Built
  each night by `.github/workflows/sync.yml` from RideTube's `main` and `sync/close.patch`; do not commit to it.
- App version: RideTube's `x.y.z` becomes `x.y.(z*100 + REV)` (`sync/REV`), so every RideTube release shows as
  an update in the Store. Raise `REV` for a change of ours alone.
- RideTube's service (`jap-ridetube-d`) still comes from RideTube's own source, `JustAnotherPU/ridetube:releases`.
