# Structured Data Notes

## Added

- Home page:
  - `ProfilePage`
  - `Person` as `mainEntity`
- Book page:
  - `Book`

## Home page fields

- `name`
- `url`
- `jobTitle`
- `description`
- `sameAs`

## Book page fields

- `name`
- `author`
- `url`
- `description`
- `inLanguage`
- `bookFormat`
- `encodingFormat`
- `image`

## Conscious omissions

- No `Organization` schema was added.
- No `Offer`, `AggregateRating`, `Review`, `ISBN`, or `publisher` fields were added.
- No extra structured data was added to `c = a + b`, `L4`, or `SER` pages.

## Why

- The local sources support a clean profile entry for the home page.
- The local sources support a book entry at repository level for `Qubit of Hope — Volume I`.
- The local sources do not provide a stable ISBN, publisher record, or commercial offer surface, so those fields were left out.
