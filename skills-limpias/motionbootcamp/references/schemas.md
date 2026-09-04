# Esquemas de Salida, Motion Creative Pipeline

Cada etapa del pipeline produce un JSON estructurado.
El campo de handoff de cada etapa es el input exacto de la siguiente.

---

## Esquema de Salida W3

```json
{
  "session_metadata": {
    "brand": "string",
    "date": "YYYY-MM-DD",
    "diagnosis": "string, 1-2 oraciones, qué debe hacer este brand con sus ads ahora",
    "diagnosis_confidence": "HIGH | MEDIUM | LOW",
    "next_diagnosis_review": "YYYY-MM-DD, fecha del próximo rediagnóstico trimestral"
  },
  "resource_gate": {
    "reviews_csv": "received | missing_using_hypothesis",
    "ads_library": "received | missing_blocked",
    "production_capacity": "number, declarado o asumido (default 3-5)",
    "atria_report": "received | not_available, validation_incomplete",
    "foreplay_boards": "received | not_available",
    "brand_guidelines": "received | will_generate_in_w4",
    "gate_status": "COMPLETE | COMPLETE_WITH_WARNINGS | BLOCKED",
    "warnings": ["string, campo faltante y su impacto en el análisis"]
  },
  "persona_analysis": {
    "ad_personas": [
      {
        "name": "string, nombre descriptivo de la persona targetada en ads",
        "description": "string, 1 oración",
        "evidence": "ads_library"
      }
    ],
    "real_personas": [
      {
        "name": "string, nombre basado en el trigger/problema",
        "trigger": "string, problema específico que causó la compra",
        "volume_rank": 1,
        "emotional_intensity": "HIGH | MEDIUM | LOW",
        "supporting_quotes": ["string, cita textual de review", "string, cita textual de review"],
        "currently_in_ads": true
      }
    ],
    "gap_detected": true,
    "gap_description": "string, descripción del gap entre persona de ads y persona real",
    "priority_personas": ["string, persona 1 para acción inmediata", "string, persona 2"]
  },
  "roadmap": {
    "production_capacity": "number, conceptos nuevos que el equipo puede producir este mes (declarado o asumido)",
    "icebox": [
      {
        "idea": "string",
        "persona": "string",
        "evidence_level": "HIGH | LOW",
        "tier": 1,
        "rationale": "string, por qué HIGH o LOW confidence",
        "sprint_slot": "NOW | NEXT_SPRINT | BACKLOG"
      }
    ],
    "sprint_now": [
      {
        "idea": "string",
        "persona": "string",
        "messaging_variations": ["string, hook 1", "string, hook 2", "string, hook 3"],
        "tier": 1,
        "evidence": "string, justificación de la evidencia",
        "production_time": "string, ej: < 1 semana",
        "lhf_priority": true
      }
    ],
    "quarterly_calendar": {
      "Q_current": "string, personas y temas asignados",
      "Q_next": "string, personas y temas asignados"
    }
  },
  "next_skill": "W4_Make_Ads",
  "w4_handoff": {
    "priority_ideas": ["string, idea 1 con mayor evidencia", "string, idea 2"],
    "priority_personas": ["string, persona 1", "string, persona 2"],
    "reference_ads": "string, URLs o descripciones de ads ganadores existentes",
    "format_recommendation": "UGC | Static | Video | Mix",
    "tier_recommendation": 1
  }
}
```

---

## Esquema de Salida W4

```json
{
  "session_metadata": {
    "brand": "string",
    "date": "YYYY-MM-DD",
    "method_used": "quick_win | animation | scalable_system",
    "persona_targeted": "string",
    "angle_used": "string"
  },
  "ads_produced": [
    {
      "ad_id": "AD-001",
      "format": "static | gif | video",
      "persona": "string",
      "angle": "string",
      "awareness_level": "TOF | MOF | BOF",
      "hook": "string, primeros 3 segundos o headline principal",
      "asset_location": "string, ruta o URL del asset",
      "production_method": "quick_win | scalable",
      "agent_scores": {
        "persona_fit": 0,
        "angle": 0,
        "emotion": 0,
        "brand_fit": 0,
        "conversion": 0,
        "grammar": 0
      }
    }
  ],
  "system_assets": {
    "brand_spec_card": "string, ruta PNG",
    "visual_style_card": "string, ruta PNG",
    "format_templates": ["string, template_1.md"],
    "agents_configured": false
  },
  "next_skill": "W5_Analyze_Ads",
  "w5_handoff": {
    "ads_to_analyze": ["AD-001"],
    "funnel_stage": "prospecting",
    "goal_metric": "string, ROAS | CPP | CPL según tipo de negocio",
    "hypothesis_per_ad": {
      "AD-001": "string, hipótesis que este ad está testeando"
    }
  }
}
```

---

## Esquema de Salida W5

```json
{
  "session_metadata": {
    "brand": "string",
    "date": "YYYY-MM-DD",
    "funnel_stage_analyzed": "prospecting",
    "goal_metric": "string, ROAS | CPP | CPL | etc.",
    "benchmark_source": "own_account | provisional"
  },
  "ad_diagnoses": [
    {
      "ad_id": "AD-001",
      "hypothesis_tested": "string, hipótesis que el ad estaba testeando",
      "result": "TRUE | TRUE_FATIGUE_WARNING | FALSE | NEEDS_MORE_TIME",
      "result_justification": "string, por qué se clasificó así",
      "fatigue_signal": {
        "detected": false,
        "frequency_7d": "number o null",
        "frequency_change_pct": "number o null, % de cambio vs semana anterior",
        "spend_trend": "stable | increasing | decreasing | null",
        "recommendation": "string, acción preventiva si detected es true, null si no"
      },
      "metrics": {
        "spend": 0,
        "first_frame_retention": "string, % o N/A",
        "thumb_stop": "string, % o N/A",
        "hold_rate": "string, % o N/A",
        "ctr": "string, % o N/A",
        "goal_metric_value": "string, número o N/A"
      },
      "bottleneck_identified": "thumbnail | hook | body_or_offer | hold | cta | landing | none",
      "bottleneck_description": "string, descripción específica",
      "bottleneck_layer": "hook_3s | body_content | offer | cta | post_click | null, capa exacta del problema",
      "action": "scale | iterate | kill | wait",
      "iteration_instruction": {
        "tier": 1,
        "specific_change": "string, instrucción exacta para el equipo creativo",
        "reference_ad": "string, ad ID del top performer a usar como referencia"
      }
    }
  ],
  "account_level_insights": {
    "winners": ["AD-001"],
    "needs_iteration": ["AD-002"],
    "kill": [],
    "pattern_detected": "string, si varios ads tienen el mismo problema",
    "org_level_implication": "string, implicación para decisiones de inversión"
  },
  "next_skill": "W6_Explore_New_USP",
  "w6_handoff": {
    "validated_angles": ["string, ángulo que resultó TRUE"],
    "failed_angles": ["string, ángulo que resultó FALSE"],
    "persona_performance": {
      "persona_name": "HIGH | MEDIUM | LOW"
    },
    "messaging_that_works": "string, descripción del messaging de los winners",
    "explore_trigger": "string, señal que indica necesidad de explorar nuevo ángulo"
  }
}
```

---

## Esquema de Salida W6

```json
{
  "session_metadata": {
    "brand": "string",
    "date": "YYYY-MM-DD",
    "exploration_trigger": "string, señal específica que disparó la exploración",
    "product_new": false,
    "harry_protocol_activated": false
  },
  "signal_analysis": {
    "language_shift_detected": true,
    "old_language": "string, terminología que está cayendo",
    "new_language": "string, terminología emergente",
    "sources": ["google_trends", "tiktok_organic", "reviews"],
    "organic_signal_strength": "HIGH | MEDIUM | LOW"
  },
  "hypothesis": {
    "statement": "string, [señal] + [asset del producto] = [hipótesis de messaging]",
    "persona_target": "string",
    "awareness_level": "TOF | MOF",
    "product_truth": "string, lo que el producto realmente hace",
    "customer_truth": "string, lo que el cliente siente/necesita",
    "claim_viability": "SAFE | REVIEW_NEEDED | REGULATED",
    "claim_notes": "string, restricciones de messaging si aplica",
    "validation_criteria": {
      "metric": "string, hook_rate | hold_rate | trial_starts | etc.",
      "threshold": "string, valor mínimo para declarar señal positiva",
      "timeframe": "string, 1 mes recomendado"
    }
  },
  "test_design": {
    "total_ads": 3,
    "ads": [
      {
        "ad_id": "EXPLORE-001",
        "format": "in_house_video | ugc_simple",
        "script_focus": "string",
        "visual_control": "string, proven formula como control visual",
        "key_difference": "string, solo el messaging cambia"
      }
    ],
    "budget_recommendation": "controlled_minimum",
    "do_not_scale_until": "string, criterio de validación que debe cumplirse"
  },
  "next_skill": "W7_Exploit_Winning_Ads",
  "w7_handoff": {
    "validated_hypothesis": "string, hipótesis a escalar si el test resulta positivo",
    "winning_ad_from_explore": "string, ad ID con mejor señal",
    "messaging_angles_to_test": ["string, angle 1", "string, angle 2"],
    "persona_to_expand": "string, persona detectada como potencial en el test",
    "scale_trigger": "string, métrica y umbral que autoriza escalar"
  }
}
```

---

## Esquema de Salida W7

```json
{
  "session_metadata": {
    "brand": "string",
    "date": "YYYY-MM-DD",
    "winner_ad_id": "string",
    "color_tag": "VERDE | SCALE_UP",
    "driver_identified": "script | talent | hook | format | emotional_driver"
  },
  "winner_deconstruction": {
    "hook": "string, descripción de los primeros 3 segundos",
    "angle": "string, ángulo estratégico",
    "format": "string, tipo de ad",
    "emotional_driver": "string, emoción que activa",
    "persona": "string"
  },
  "ad_family": {
    "easy_scales": [
      {
        "ad_id": "SCALE-001",
        "iteration_type": "visual_refresh | talent_refresh | format_test | length_test | message_order | placement_adaptation",
        "change_made": "string",
        "what_stays_same": "string",
        "andromeda_signal": "string, por qué genera señal nueva para el algoritmo",
        "placement_details": {
          "source_format": "string, ej: 9:16",
          "target_format": "string, ej: 1:1 o 4:5",
          "text_overlay_required": false,
          "overlay_rationale": "string, qué información visual se pierde con el reencuadre y cómo compensarla"
        }
      }
    ],
    "expansion_phase": [
      {
        "ad_id": "EXPAND-001",
        "iteration_type": "persona_pivot | new_angle | mashup | net_new_concept",
        "change_made": "string",
        "new_element": "string",
        "what_stays_same": "string"
      }
    ],
    "total_ads_planned": 0,
    "batches": [
      {
        "batch_number": 1,
        "ads": ["SCALE-001"],
        "batch_focus": "string, qué se testea en este batch"
      }
    ]
  },
  "ugc_program": {
    "activated": false,
    "content_buckets": {
      "evergreen_bau": "string",
      "product_launches": "string",
      "seasonal": "string"
    }
  },
  "concept_formulas": [
    {
      "concept_title": "string",
      "angle": "string, por qué funciona",
      "creative_guardrails": "string, tono, delivery, restricciones",
      "objection_handling": "string, objeción → reframe"
    }
  ],
  "refresh_plan": {
    "fatigue_signal": "string, métrica y umbral que indica fatiga",
    "refresh_trigger": "winner fatigues AND all iterations stop working",
    "refresh_brief": "string, descripción de V2.0: mismo alma, nueva producción"
  },
  "pipeline_complete": true,
  "hard_pivot_triggered": false,
  "hard_pivot_reason": "string o null, solo si todos los conceptos fallaron de forma sistémica",
  "atria_veto": false,
  "atria_veto_reason": "string o null, describe el conflicto entre ROAS Meta y rentabilidad real de Atria",
  "next_cycle": "W3_Prioritize_Ad_Ideas",
  "w3_rediagnosis_trigger": "string, señal que indica que el diagnóstico debe actualizarse",
  "feedback_loop": {
    "winners_validated": [
      {
        "ad_id": "string",
        "angle": "string, el ángulo que el mercado validó",
        "persona": "string",
        "w3_evidence_level": "HIGH_CONFIDENCE, se convierte en evidencia base del próximo roadmap"
      }
    ],
    "personas_confirmed": [
      {
        "name": "string",
        "performance": "string, ROAS o métrica de performance que confirma la persona",
        "w3_priority": "FIRST_SPRINT, prioridad automática en el próximo W3"
      }
    ],
    "angles_exhausted": [
      {
        "angle": "string",
        "reason": "fatigued | no_signal | hard_pivot",
        "w3_icebox_tag": "DO_NOT_REPEAT_YET"
      }
    ],
    "atria_validation": {
      "roas_meta": "number o null",
      "roas_real_atria": "number o null",
      "delta": "string o null, diferencia entre ambos",
      "scale_authorized": true
    }
  }
}
```
