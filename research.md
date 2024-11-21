---
title: Research
short_title: Research
downloads:
  - file: null
    title: null
---

### Analyzing Embeddings of Prompts

[Webpage](embeddings) | [GitHub Repository](https://github.com/Tiger-Du/SE-PINN)

---

<!-- ### [SE-PINN](sepinn) -->

### SE-PINN

[Webpage](sepinn) | [GitHub Repository](https://github.com/Tiger-Du/SE-PINN)

__Summary__: The mathematical properties of __normality__, __symmetry__, and __orthogonality__ are integrated into a neural network in PyTorch via a __custom loss function__ and a __custom architectural layer__ so that its predictions respect these properties by design.

__Figure__: The prediction of the __energy eigenvector__ (left) appears to converge, but the prediction of the __energy eigenvalue__ (right) is slower. Visit the repository to see the same visualization when the model is constrained to respect __symmetry__ in its predictions.

```{image} ./images/no_enforcement_of_symmetry.gif
:alt: Animation of PINN
:align: center
```

---
